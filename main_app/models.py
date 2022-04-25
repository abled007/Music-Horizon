from django.db import models
from django.contrib.auth.models import User
#Create your models here.

class Song(models.Model):

    title = models.CharField(max_length=20)
    artist = models.CharField(max_length=60)
    audio_link = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Playlist(models.Model):

    title = models.CharField(max_length=20)
    songs = models.ManyToManyField(Song)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

