from functools import partial
from django.conf import settings
import os


def dir_from_instance(instance, dirs):
    return os.path.join(f'{instance.author}_{instance.author.pk}', *dirs)


def media_dir_from_instance(instance, dirs):
    return os.path.join(settings.MEDIA_ROOT, dir_from_instance(instance, dirs))


def file_upload_to(instance, filename, dirs):
    return dir_from_instance(instance, dirs) + filename


thumbnail_file_upload_to = partial(file_upload_to, dirs=('thumbnail/',))


def game_dir_from_instance(instance):
    return media_dir_from_instance(instance, ('game', instance.slug))
