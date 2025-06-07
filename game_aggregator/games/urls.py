from django.urls import path
from .views import game_list, filtre_date, filtre_simulation, filtre_adventure, filtre_rpg, filtre_horror, filtre_simulator, filtre_platformer, filtre_strategy, filtre_shooter, filtre_action


urlpatterns = [
    path('', game_list, name='game_list'),
    path('filtre_date', filtre_date, name='filtre_date'),
    path('filtre_simulation', filtre_simulation, name='filtre_simulation'),
    path('filtre_adventure', filtre_adventure, name='filtre_adventure'),
    path('filtre_rpg', filtre_rpg, name='filtre_rpg'),
    path('filtre_horror', filtre_horror, name='filtre_horror'),
    path('filtre_simulator', filtre_simulator, name='filtre_simulator'),
    path('filtre_platformer', filtre_platformer, name='filtre_platformer'),
    path('filtre_strategy', filtre_strategy, name='filtre_strategy'),
    path('filtre_shooter', filtre_shooter, name='filtre_shooter'),
    path('filtre_action', filtre_action, name='filtre_action'),




]

