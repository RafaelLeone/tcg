# Generated by Django 4.2.11 on 2024-03-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkmn_tcg', '0004_rename_attack_1_effect_pokemoncard_ability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemoncard',
            name='attack_2_cost',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='pokemoncard',
            name='attack_2_effects',
            field=models.JSONField(blank=True, default=list),
        ),
    ]