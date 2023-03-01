from django.db import models
from django.urls import reverse
from django.utils.text import slugify


from users import models as users_models


class Game(models.Model):
  slug = models.SlugField(max_length=80)
  title = models.CharField(max_length=80)
  author = models.ForeignKey(
      users_models.Profile, on_delete=models.SET_NULL, related_name='own_games', null=True)
  description = models.TextField()
  thumbnail = models.ImageField(upload_to='thumbnails/')
  js_script_file = models.FileField(upload_to='js_game_scripts/')

  class Meta:
    ordering = ['title']

  def get_absolute_url(self):
    return reverse('game', kwargs={'name': self.slug})


class GameResult(models.Model):
  profile = models.ForeignKey(
      users_models.Profile, on_delete=models.CASCADE, related_name='game_results')
  points = models.IntegerField(default=0)
  game = models.ForeignKey(
      Game, on_delete=models.CASCADE, related_name='game_results')
