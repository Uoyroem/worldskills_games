import os

from django.conf import settings
from django.core.validators import FileExtensionValidator

from django.db import models
from django.urls import reverse

from ..users import models as users_models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .utils import upload_to
from .services import game_creation


class Game(models.Model):
    slug = models.SlugField('Url', max_length=80)
    title = models.CharField(max_length=80)
    author = models.ForeignKey(
        users_models.Profile, on_delete=models.SET_NULL, related_name='own_games', null=True)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    play_count = models.IntegerField(default=0)
    game_zip = models.FileField(upload_to='games',
                                validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    extracting_script = models.CharField(verbose_name='Script for extracting the result',
                                         max_length=255,
                                         default='result_extracting.js')

    thumbnail = models.CharField(max_length=255,
                                 default='thumbnail.png')
    html = models.CharField(max_length=255,
                            default='index.html')

    @property
    def html_url(self):
        return os.path.join(self.get_absolute_url(), self.html)

    @property
    def extracting_script_url(self):
        return os.path.join(self.get_absolute_url(), self.extracting_script)

    @property
    def thumbnail_url(self):
        return os.path.join(self.get_absolute_url(), self.thumbnail)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_delete_url(self):
        return reverse('games:delete', kwargs={'slug': self.slug})

    def get_manage_url(self):
        return reverse('games:manage', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('games:detail', kwargs={'slug': self.slug})


@receiver(pre_delete, sender=Game)
def _(sender, instance, **kwargs):
    game_creation.remove_game_in_media(instance)


class GameResult(models.Model):
    profile = models.ForeignKey(
        users_models.Profile, on_delete=models.CASCADE, related_name='game_results')
    points = models.IntegerField(default=0)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='game_results')
