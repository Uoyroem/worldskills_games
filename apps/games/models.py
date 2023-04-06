import os

from django.conf import settings
from django.core.validators import FileExtensionValidator

from django.db import models
from django.urls import reverse

from ..users import models as users_models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .utils import upload_to


class Game(models.Model):
    slug = models.SlugField('Url', max_length=80)
    title = models.CharField(max_length=80)
    author = models.ForeignKey(
        users_models.Profile, on_delete=models.SET_NULL, related_name='own_games', null=True)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    play_count = models.IntegerField(default=0)
    game_zip = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    script = models.CharField(max_length=255,
                              default='index.js')
    thumbnail = models.CharField(max_length=255,
                                 default='thumbnail.png')
    html = models.CharField(max_length=255,
                            default='index.html')

    @property
    def html_url(self):
        return os.path.join('http://localhost:8000/', self.get_absolute_url().removeprefix('/'), self.html)

    @property
    def script_url(self):
        return os.path.join(self.get_absolute_url(), self.script)

    @property
    def thumbnail_url(self):
        return os.path.join(self.get_absolute_url(), self.thumbnail)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('games:game-detail', kwargs={'slug': self.slug})

    def get_api_url(self):
        return reverse('game-detail', kwargs={'pk': self.pk})


class GameResult(models.Model):
    profile = models.ForeignKey(
        users_models.Profile, on_delete=models.CASCADE, related_name='game_results')
    points = models.IntegerField(default=0)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='game_results')
