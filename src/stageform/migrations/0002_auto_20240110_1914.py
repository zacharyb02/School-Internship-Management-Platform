# Generated by Django 3.1.6 on 2024-01-10 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stageform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entreprises',
            old_name='contact',
            new_name='entreprise_contact',
        ),
        migrations.RenameField(
            model_name='entreprises',
            old_name='fax',
            new_name='entreprise_fax',
        ),
        migrations.RenameField(
            model_name='entreprises',
            old_name='tel_contact',
            new_name='entreprise_tel_contact',
        ),
        migrations.RenameField(
            model_name='entreprises',
            old_name='telephone',
            new_name='entreprise_telephone',
        ),
    ]
