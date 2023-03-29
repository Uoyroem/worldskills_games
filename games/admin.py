from django.contrib import admin
from . import models


class GameModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'updated_time']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Game, GameModelAdmin)
admin.site.register(models.GameResult)
