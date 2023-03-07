from functools import partial

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from users import models as users_models


def game_file_upload_to(dirname: str, instance: 'Game', filename: str):
  return f'user_{instance.author.pk}/{dirname}/{filename}'


game_files_upload_to = partial(game_file_upload_to, 'games')
game_thumbnail_upload_to = partial(game_file_upload_to, 'thumbnails')


def game_zip_info_default():
  return {
      'script_paths': [],
      'assets': {}
  }


class Game(models.Model):
  slug = models.SlugField('Url', max_length=80)
  title = models.CharField(max_length=80)
  author = models.ForeignKey(
      users_models.Profile, on_delete=models.SET_NULL, related_name='own_games', null=True)
  description = models.TextField()
  thumbnail = models.ImageField(upload_to=game_thumbnail_upload_to)

  game_zip = models.FileField(upload_to=game_files_upload_to)
  game_zip_info = models.JSONField(default=game_zip_info_default)
  created_time = models.DateTimeField(auto_now_add=True)
  updated_time = models.DateTimeField(auto_now=True)
  play_count = models.IntegerField(default=0)

  class Meta:
    ordering = ['title']

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('game', kwargs={'slug': self.slug})

  def get_script_urls(self):
    return self.game_zip_info['script_paths']

  def get_assets(self):
    return self.game_zip_info['assets']


class GameResult(models.Model):
  profile = models.ForeignKey(
      users_models.Profile, on_delete=models.CASCADE, related_name='game_results')
  points = models.IntegerField(default=0)
  game = models.ForeignKey(
      Game, on_delete=models.CASCADE, related_name='game_results')
