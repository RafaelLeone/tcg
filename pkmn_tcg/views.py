from django.shortcuts import render
from .models import PokemonCard


def pokemon_list(request):
    pokemon_cards = PokemonCard.objects.all()
    return render(request, 'pkmn_tcg/pokemon_list.html', {'pokemon_cards': pokemon_cards})

def pokemon_detail(request, pk):
    pokemon_card = PokemonCard.objects.get(pk=pk)
    return render(request, 'pkmn_tcg/pokemon_detail.html', {'pokemon_card': pokemon_card})
