from contextlib import suppress
from django.core.exceptions import ObjectDoesNotExist

from django import template
from .. import models

register = template.Library()


@register.simple_tag
def game_result_from_game_and_profile(game, profile):
    with suppress(ObjectDoesNotExist):
        return models.GameResult.objects.get(game=game, profile=profile)


