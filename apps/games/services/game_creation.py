import zipfile
from django.conf import settings
import os
import shutil


def game_media_path(instance) -> str:
    return os.path.join(
        settings.MEDIA_ROOT,
        instance.get_absolute_url().removeprefix('/')
    )


def extract_zip_to_media(instance, file) -> None:
    with zipfile.ZipFile(file) as game_zip:
        game_zip.extractall(
            path=game_media_path(instance)
        )


def remove_game_in_media(instance) -> None:
    shutil.rmtree(game_media_path(instance))
    os.remove(instance.game_zip.path)
