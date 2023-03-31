from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameListView.as_view(), name='index'),
    path('game/<slug:slug>', views.GameView.as_view(), name='game'),
    path('create_new_game', views.GameCreateView.as_view(), name='create_new_game'),
    path('manage_games', views.ManageGameView.as_view(), name='manage_games'),

]
