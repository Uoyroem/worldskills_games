
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import F

from rest_framework import viewsets, mixins

from . import models
from . import forms
from . import serializers


class GameList(ListView):
    template_name = 'games/index.html'
    model = models.Game
    filter_choices = {
        'popularity': 'play_count',
        'recently_updated': 'updated_time',
        'alphabetically': 'title'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_filter'] = self.get_current_filter()
        context['current_sort'] = self.get_current_sort()
        context['filter_choices'] = self.filter_choices
        return context

    def get_current_filter(self):
        return self.filter_choices[self.request.GET.get('filter', 'popularity')]

    def get_current_sort(self):
        return self.request.GET.get('sort', 'desc')

    def get_ordering(self):
        current_sort_filter = self.get_current_sort()
        current_filter = self.get_current_filter()
        if current_sort_filter == 'desc':
            return '-' + current_filter
        elif current_sort_filter == 'asc':
            return current_filter


class GameCreate(LoginRequiredMixin, CreateView):
    form_class = forms.GameCreationForm
    template_name = 'games/game_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class GameDetailView(DetailView):
    model = models.Game

    def get_object(self, queryset=None):
        game = super().get_object(queryset)
        game.play_count = F('play_count') + 1
        game.save()
        return game


class ManageGameView(ListView):
    model = models.Game
    template_name = 'games/manage_games.html'

    def get_queryset(self):
        return super().get_queryset().filter(author__user=self.request.user)


class GameViewSet(mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
