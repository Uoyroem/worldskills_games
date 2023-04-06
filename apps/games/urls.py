from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('games/', views.GameListView.as_view(), name='game-list'),
    path('games/<slug:slug>', views.GameView.as_view(), name='game-detail'),
    path('create-new-game', views.GameCreateView.as_view(), name='create-new-game'),
    path('manage-games', views.ManageGameView.as_view(), name='manage-games'),
]
