from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Song, Musician


class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Musician_key',)}


admin.site.register(Song, SongAdmin)
admin.site.register(Musician)

