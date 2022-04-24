from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Song, Playlist
from django.views.generic.edit import CreateView


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

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

class Playlist_Create(CreateView):
    model = Playlist
    fields = ['title', 'songs']
    template_name = 'playlist_create.html'
    success_url = '/songs/'

