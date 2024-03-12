# pkmn_tcg/urls.py

from django.urls import path
from .views import pokemon_list, pokemon_detail

urlpatterns = [
    path('pokemon/', pokemon_list, name='pokemon_list'),
    path('pokemon/<int:pk>/', pokemon_detail, name='pokemon_detail'),
]
