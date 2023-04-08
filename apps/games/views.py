import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, mixins
import zipfile


from . import forms
from . import models
from . import serializers


class GameListView(ListView):
    template_name = 'games/game_list.html'
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


class GameCreateView(LoginRequiredMixin, CreateView):
    form_class = forms.GameForm
    template_name = 'games/game_form.html'
    success_url = reverse_lazy('games:game-list')
    login_url = reverse_lazy('users:signin')

    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user.profile
        if settings.DEBUG:
            with zipfile.ZipFile(form.instance.game_zip) as game_zip:
                game_zip.extractall(
                    path=os.path.join(
                        settings.MEDIA_ROOT,
                        form.instance.get_absolute_url().removeprefix('/')
                    )
                )
        return super().form_valid(form)


class GameView(DetailView):
    model = models.Game

    def get_context_data(self, **kwargs):
        from contextlib import suppress
        context = super().get_context_data(**kwargs)
        context['game_result_form'] = forms.GameResultForm(data={
            'points': 0
        })

        with suppress(ObjectDoesNotExist):
            context['profile_game_result'] = (self.request.user
                                              and self.request.user.profile.game_results.get(game=context['object']))
        return context

    def post(self, request, slug):
        game = self.get_queryset().get(slug=slug)

        try:
            points = int(request.POST.get('points'))
            game_result = self.request.user.profile.game_results.get(game=game)
            if points > game_result.points:
                game_result.points = points
                game_result.save()
        except ObjectDoesNotExist:
            form = forms.GameResultForm(request.POST)
            game_result = form.save(commit=False)
            game_result.profile = self.request.user.profile
            game_result.game = game
            game_result.save()
        finally:
            return redirect(game.get_absolute_url(), permament=True)

    def get_object(self, queryset=None):
        game = super().get_object(queryset)
        game.play_count = F('play_count') + 1
        game.save()
        return game


class ManageGameView(LoginRequiredMixin, UpdateView):
    form_class = forms.GameForm
    model = models.Game
    template_name = 'games/manage_game.html'
    login_url = reverse_lazy('users:signin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user.profile)


class GameDeleteView(LoginRequiredMixin, UpdateView):
    model = models.Game
    fields = '__all__'
    success_url = reverse_lazy('games:list')
