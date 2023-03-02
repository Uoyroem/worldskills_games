from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.GameList.as_view(), name='index'),
    # path('game/<slug:name>', views.index),
    path('create_new_game', views.GameCreate.as_view(), name='create_new_game')
]
