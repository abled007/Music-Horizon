from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Song


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

# class Song:
#     def __init__(self, title, artist, audio_link):
#         self.title = title
#         self.artist = artist
#         self.audio_link = audio_link

# songs = [
#     Song('Power Trip', 'J. Cole', 'https://open.spotify.com/embed/track/7FOJvA3PxiIU0DN3JjQ7jT?si=fb0ae669971a42e0'),
# ]

class SongList(TemplateView):
    template_name = 'songlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get('title')
        if title != None:
            context['songs'] = Song.objects.filter(title__icontains=title)
        else:
            context['songs'] = Song.objects.all()
        return context