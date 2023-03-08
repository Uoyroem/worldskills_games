from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.GameList.as_view(), name='index'),
    path('game/<slug:slug>', views.GameDetailView.as_view(), name='game'),
    path('create_new_game', views.GameCreate.as_view(), name='create_new_game'),
    path('manage_games', views.ManageGameView.as_view(), name='manage_games'),
    path('game/<int:pk>/change', views.change_game, name='change_game'),
    path('game/<int:pk>/delete', views.delete_game, name='delete_game')
]
