from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Song, Playlist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class Playlist_Create(CreateView):
    model = Playlist
    fields = '__all__'
    template_name = 'playlist_create.html'
    # success_url = 'playlists/'
    def get_success_url(self):
        return reverse('playlist-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/playlists')

class Playlist_Detail(DetailView):
    model = Playlist
    template_name = 'playlist_detail.html'

class Playlist_Update(UpdateView):
    model = Playlist
    fields = '__all__'
    template_name = 'playlist_update.html'
    # success_url = '/playlists'
    def get_success_url(self):
        return reverse('playlist-detail', kwargs={'pk': self.object.pk})

class Playlist_Delete(DeleteView):
    model = Playlist
    template_name = 'playlist_delete_confirm.html'
    success_url = '/playlists/'


class Playlist_View(TemplateView):
    template_name = 'playlists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists'] = Playlist.objects.all()
        return context


def profile(request, username):
    user = User.objects.get(username=username)
    playlists = Playlist.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'playlists': playlists})

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
        

