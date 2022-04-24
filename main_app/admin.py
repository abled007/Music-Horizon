from django.contrib import admin
from .models import Song, Playlist

# Register your models here.

admin.site.register(Song)
admin.site.register(Playlist)