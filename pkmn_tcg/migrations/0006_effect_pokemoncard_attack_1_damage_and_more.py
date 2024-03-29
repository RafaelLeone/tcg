# Generated by Django 4.2.11 on 2024-03-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkmn_tcg', '0005_alter_pokemoncard_attack_2_cost_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='attack_1_damage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='attack_2_damage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='pokemoncard',
            name='attack_1_effects',
        ),
        migrations.RemoveField(
            model_name='pokemoncard',
            name='attack_2_effects',
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='ability_effects',
            field=models.ManyToManyField(blank=True, related_name='ability_effects', to='pkmn_tcg.effect'),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='attack_1_effects',
            field=models.ManyToManyField(blank=True, related_name='attack_1_effects', to='pkmn_tcg.effect'),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='attack_2_effects',
            field=models.ManyToManyField(blank=True, related_name='attack_2_effects', to='pkmn_tcg.effect'),
        ),
    ]
