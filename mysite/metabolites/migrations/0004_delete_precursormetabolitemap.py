# Generated by Django 3.1.4 on 2021-02-05 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metabolites', '0003_delete_precursors'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrecursorMetaboliteMap',
        ),
    ]