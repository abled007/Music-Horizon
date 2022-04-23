from django.db import models

#Create your models here.

class Song(models.Model):

    title = models.CharField(max_length=20)
    artist = models.CharField(max_length=60)
    img = models.CharField(max_length=500)
    audio_link = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
