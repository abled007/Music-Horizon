from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Song, Playlist
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User


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

class Playlist(TemplateView):
    template_name = 'playlists.html'

# class Playlist_Create(CreateView):
#     model = Playlist
#     fields = '__all__'
#     template_name = 'playlist_create.html'
#     success_url = '/playlists/'

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect('/playlists')
        
# def profile(request, username):
#     user = User.objects.get(username=username)
#     playlists = Playlist.objects.filter(user=user)
#     return render(request, 'profile.html', {'username': username, 'playlists': playlists})
