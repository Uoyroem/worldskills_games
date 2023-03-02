from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView, ListView, CreateView
from . import models
from . import forms


class GameList(ListView):
  model = models.Game


class GameCreate(CreateView):
  form_class = forms.GameCreationForm
  template_name = 'games/game_form.html'
  success_url = reverse_lazy('index')

  def form_valid(self, form) -> HttpResponse:
    form.instance.author = self.request.user.profile
    return super().form_valid(form)
