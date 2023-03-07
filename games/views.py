import zipfile
from io import BytesIO

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import default_storage
from django.core.files.base import File
from django.db.models import F

from . import models
from . import forms


class GameList(ListView):
  model = models.Game
  filter_choices = {
      'popularity': 'play_count',
      'recently_updated': 'updated_time',
      'alphabetically': 'title'
  }

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['current_filter'] = self.get_current_filter()
    context['filter_choices'] = self.filter_choices
    return context

  def get_current_filter(self):
    return self.filter_choices[self.request.GET.get('filter', 'popularity')]

  def get_ordering(self):
    return '-' + self.get_current_filter()


class GameCreate(LoginRequiredMixin, CreateView):
  form_class = forms.GameCreationForm
  template_name = 'games/game_form.html'
  success_url = reverse_lazy('index')

  def form_valid(self, form) -> HttpResponse:
    form.instance.author = self.request.user.profile

    with zipfile.ZipFile(form.files['game_zip']) as game_zip:
      for file in game_zip.filelist:
        if file.is_dir():
          continue
        io = BytesIO(game_zip.read(file.orig_filename))
        dir_ = models.game_files_upload_to(
            form.instance, ''.join(form.instance.title + '/' + file.filename))
        default_storage.save(dir_, File(io))
        if file.filename.split('.')[-1] == 'js':
          form.instance.game_zip_info['script_paths'].append('/media/' + dir_)
        else:
          form.instance.game_zip_info['assets'][file.filename.split(
              '/')[-1]] = '/media/' + dir_
    return super().form_valid(form)


class GameDetailView(DetailView):
  model = models.Game

  def get_object(self, queryset=None):
    game = super().get_object(queryset)
    game.play_count = F('play_count') + 1
    game.save()
    return game
