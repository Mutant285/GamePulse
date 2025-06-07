from django.shortcuts import render
from .models import Game

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})


def filtre_date(request):
    games = Game.objects.order_by('-date')
    return render(request, 'games/game_list.html', {'games': games})


def filtre_simulation(request):
    games = Game.objects.filter(genre__contains='Simulation')
    return render(request, 'games/game_list.html', {'games': games})


def filtre_adventure(request):
    games = Game.objects.filter(genre__contains='Adventure')
    return render(request, 'games/game_list.html', {'games': games})



def filtre_rpg(request):
    games = Game.objects.filter(genre__contains='RPG')
    return render(request, 'games/game_list.html', {'games': games})


def filtre_strategy(request):
    games = Game.objects.filter(genre__contains='Strategy')
    return render(request, 'games/game_list.html', {'games': games})


def filtre_action(request):
    games = Game.objects.filter(genre__contains='Action ')
    return render(request, 'games/game_list.html', {'games': games})


def filtre_shooter(request):
    games = Game.objects.filter(genre__contains='Shooter ')
    return render(request, 'games/game_list.html', {'games': games})


def filtre_horror(request):
    games = Game.objects.filter(genre__contains='Horror ')
    return render(request, 'games/game_list.html', {'games': games})


def filtre_simulator(request):
    games = Game.objects.filter(genre__contains='Simulator')
    return render(request, 'games/game_list.html', {'games': games})


def filtre_platformer(request):
    games = Game.objects.filter(genre__contains='Platformer')
    return render(request, 'games/game_list.html', {'games': games})