
from django.db import models
from django.urls import reverse

from users import models as users_models


def thumbnail_file_upload_to(instance: 'Game', filename: str):
    return f'{instance.author}_{instance.author.pk}/thumbnail/{filename}'


class Game(models.Model):
    slug = models.SlugField('Url', max_length=80)
    title = models.CharField(max_length=80)
    author = models.ForeignKey(
        users_models.Profile, on_delete=models.SET_NULL, related_name='own_games', null=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to=thumbnail_file_upload_to)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    play_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game', kwargs={'slug': self.slug})

    def get_absolute_api_url(self):
        return reverse('game-detail', kwargs={'pk': self.pk})


class GameResult(models.Model):
    profile = models.ForeignKey(
        users_models.Profile, on_delete=models.CASCADE, related_name='game_results')
    points = models.IntegerField(default=0)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='game_results')
