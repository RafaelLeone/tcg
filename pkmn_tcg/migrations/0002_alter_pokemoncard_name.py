# Generated by Django 4.2.11 on 2024-03-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkmn_tcg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemoncard',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
