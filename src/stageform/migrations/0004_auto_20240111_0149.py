# Generated by Django 3.1.6 on 2024-01-11 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stageform', '0003_auto_20240111_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effectuer',
            name='annee',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='effectuer',
            name='code_type',
            field=models.CharField(max_length=2),
        ),
    ]
