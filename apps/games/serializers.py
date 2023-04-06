
from rest_framework import serializers

from . import models


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = ['slug', 'description', 'title', 'slug', 'thumbnail']
