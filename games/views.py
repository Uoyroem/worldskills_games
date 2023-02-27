from django.shortcuts import render
from . import models


def index(request):
  games = models.Game.objects.all()
  context = {
      'games': games
  }
  return render(request, 'games/index.html', context)
