from django.db import models

# Create your models here.
class Effect(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class PokemonCard(models.Model):
    CARD_TYPES = [
        ('pokemon', 'Pokemon'),
        ('trainer', 'Trainer'),
        ('energy', 'Energy'),
    ]

    ENERGY_TYPES = [
        ('colorless', 'Colorless'),
        ('grass', 'Grass'),
        ('fire', 'Fire'),
        ('water', 'Water'),
        ('lightning', 'Lightning'),
        ('fighting', 'Fighting'),
        ('psychic', 'Psychic'),
    ]

    STATUS_CHOICES = [
        ('normal', 'Normal'),
        ('burned', 'Burned'),
        ('poisoned', 'Poisoned'),
        ('asleep', 'Asleep'),
        ('confused', 'Confused'),
        ('paralyzed', 'Paralyzed'),
        # Add more status types as needed
    ]

    STAGE_CHOICES = [
        ('basic', 'Basic'),
        ('stage1', 'Stage 1'),
        ('stage2', 'Stage 2'),
    ]

    name = models.CharField(max_length=100, unique=True)
    card_type = models.CharField(max_length=10, choices=CARD_TYPES)
    hp = models.IntegerField(null=True, blank=True)
    pokemon_type = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='normal')
    ability = models.TextField(null=True, blank=True)

    attack_1_name = models.CharField(max_length=100, null=True, blank=True)
    attack_1_cost = models.JSONField(default=list)  # List to represent energy costs
    attack_1_damage = models.IntegerField(null=True, blank=True)  # New field for attack damage

    attack_2_name = models.CharField(max_length=100, null=True, blank=True)
    attack_2_cost = models.JSONField(default=list, blank=True)  # Allow an empty list for no second attack
    attack_2_damage = models.IntegerField(null=True, blank=True)  # New field for attack damage

    attack_1_effects = models.ManyToManyField(Effect, related_name='attack_1_effects', blank=True)
    attack_2_effects = models.ManyToManyField(Effect, related_name='attack_2_effects', blank=True)
    ability_effects = models.ManyToManyField(Effect, related_name='ability_effects', blank=True)

    weakness = models.CharField(max_length=50, null=True, blank=True)
    resistance = models.CharField(max_length=50, null=True, blank=True)
    retreat_cost = models.IntegerField(null=True, blank=True)
    stage = models.CharField(max_length=10, choices=STAGE_CHOICES, null=True, blank=True)
    evolves_from = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Deck(models.Model):
    name = models.CharField(max_length=100)
    cards = models.ManyToManyField(PokemonCard)
    # Add other attributes specific to your decks

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    # Add other attributes specific to your players

    def __str__(self):
        return self.name
