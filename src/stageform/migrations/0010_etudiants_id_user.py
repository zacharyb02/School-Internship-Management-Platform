# Generated by Django 3.1.6 on 2024-01-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stageform', '0009_auto_20240111_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiants',
            name='id_user',
            field=models.IntegerField(default=1, unique=True),
        ),
    ]
