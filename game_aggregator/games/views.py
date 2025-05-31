from django.shortcuts import render
from .models import Game

def game_list(request):
    games = Game.objects.order_by('-date')
    return render(request, 'games/game_list.html', {'games': games})

