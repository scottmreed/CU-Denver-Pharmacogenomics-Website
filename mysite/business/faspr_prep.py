import pickle5 as pickle
from mysite.business.alderaan import Alderaan
from Bio import SeqUtils
from Bio.PDB import PPBuilder
from Bio.PDB.PDBParser import PDBParser
import os


class FasprPrep:
    P_num = ''
    mutation_position = 0
    CCID = ''
    gene_ID = ''
    unzip_target_pdb_file = 'tmp.pdb'
    sur_aa_low = ''
    sur_aa_high = ''
    unmutated_seq = ''
    single_nucleotide = ''
    single_nucleotide_variation = ''
    mutated_protein_code = ''
    alderaan = None
    neighbors = 7
    scratch_folder = os.path.join('/','storage','chemistry','projects','pharmacogenomics')
    alpha_folder = os.path.join(scratch_folder, 'alphafold')
    temp_folder = os.path.join(scratch_folder, 'tmp')

    def __init__(self, CCID, gene_ID):
        self.alderaan = Alderaan()
        self.CCID = CCID
        self.gene_ID = gene_ID
        self.get_Pnum()
        self.unmutated_seq = self.get_sequence_unmut()
        self.get_mut_pos = self.get_mutation_position(CCID)
        self.get_mut_seq = self.get_mutated_sequence(self.unmutated_seq)
        # self.client = alderaan.paramiko.client.SSHClient()

    def get_Pnum(self):
        with open('../pharmacogenomics_website/resources/ENSG_PN_dictALL.pickle', 'rb') as f:
            ENSG_Pnum_dict = pickle.load(f)
            self.P_num = ENSG_Pnum_dict[f'{self.gene_ID}']
        print('P_num is',self.P_num)

    def get_sequence_unmut(self):
        # return ('sampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstringsampleproteinstring')
        p = PDBParser()
        protein_count_command = f'ls -dq {self.alpha_folder}/AF-{self.P_num}-F*-model_v* | wc -l'
        protein_count, success = self.alderaan.run_command(protein_count_command)
        if success:
            protein_number = int(protein_count)
            if protein_number == 2:
                protein_filename = f"find '{self.alpha_folder}' -maxdepth 1 -name 'AF-{self.P_num}-F*-model_v*.pdb.gz'"
                pdb_file, success = self.alderaan.run_command(protein_filename)
                _ , protein_short_name = os.path.split(pdb_file[:-4])
                self.alderaan.run_command(f'gunzip -k {pdb_file} > {self.temp_folder}/{protein_short_name}')
                structure = p.get_structure('xx',f'{self.temp_folder}/{protein_short_name}')
                ppb = PPBuilder()
                pp = ppb.build_peptides(structure)
                PDBs = str(pp.get_sequence())
                unmutated_sequence = PDBs.lower()
                return unmutated_sequence
            else:
                print('protein in multiple files. Skipped.')

    def get_mutation_position(self, poss_mutation):
        if poss_mutation.startswith('p.') \
                and poss_mutation[2:5] != poss_mutation[-3:] \
                and poss_mutation[-3:] != 'del' \
                and poss_mutation[-3:] != 'Ter' and poss_mutation[-3:] != 'dup' \
                and len(poss_mutation) < 12:
            act_mutation = poss_mutation.split(' ')
            for mutation in act_mutation:
                mutation_position = int(mutation[5:-3])
                return mutation_position

    def get_mutated_sequence(self, seq):
        position_mutation = self.get_mutation_position(self.CCID)
        self.mutated_protein_code = self.unmutated_seq[0:position_mutation - self.neighbors] + \
                               self.sur_aa_low + \
                               self.unmutated_seq[position_mutation - 1]\
                                   .replace(self.single_nucleotide,
                                            self.single_nucleotide_variation) + self.sur_aa_high + \
                                            self.unmutated_seq[position_mutation + 6:]
        return self.mutated_protein_code

    def make_mutatedseq_file(self, mutatseq):
        mutated_seq_file = open(f"repack_{self.P_num}_{self.CCID[2:]}.txt", "w")
        mutated_seq_file.close()
        return mutated_seq_file.write(f"{self.mutated_protein_code}")

    def get_specific_mutation(self):
        poss_mutation_ext = self.CCID
        possible_mutation_ext = str(poss_mutation_ext)
        position_mutation = self.get_mutation_position(possible_mutation_ext)

        INV = possible_mutation_ext[2:5]
        MNV = possible_mutation_ext[-3:]
        self.sur_aa_low = self.unmutated_seq[position_mutation - self.neighbors:position_mutation - 1].upper()
        self.sur_aa_high = self.unmutated_seq[position_mutation:position_mutation + 6].upper()
        self.single_nucleotide = SeqUtils.IUPACData.protein_letters_3to1[f'{INV}'].lower()
        self.single_nucleotide_variation = SeqUtils.IUPACData.protein_letters_3to1[f'{MNV}']
        if self.unmutated_seq[position_mutation - 1] == f'{self.single_nucleotide}':
            mutated_protein_code = self.get_mutated_sequence(self.unmutated_seq)
            self.make_mutatedseq_file(mutated_protein_code)
        self.alderaan.run_command(f"singularity shell /storage/singularity/qvina.sif")
        self.alderaan.run_command(
            f"/FASPR/FASPR -i /{self.scratch_folder}{self.unzip_target_pdb_file} -s /{self.scratch_folder}/repack_lines/repack_{self.P_num}_{possible_mutation_ext[2:]}.txt  -o /{self.scratch_folder}/proteinmutations/{self.P_num}_{self.possible_mutation_ext}_FASPR.pdb")
