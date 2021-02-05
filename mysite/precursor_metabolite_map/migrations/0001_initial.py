# Generated by Django 3.1.4 on 2021-02-05 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrecursorMetaboliteMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precursor_UUID', models.CharField(max_length=36, verbose_name='precursor_UUID')),
                ('metabolite_UUID', models.CharField(max_length=36, verbose_name='metabolite_UUID')),
                ('origin', models.CharField(max_length=12, verbose_name='origin')),
            ],
            options={
                'db_table': 'precursor_metabolite_map',
                'managed': True,
            },
        ),
    ]