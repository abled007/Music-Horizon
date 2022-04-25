from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('user/<username>/', views.profile, name='profile'),
    path('songs/', views.SongList.as_view(), name='song-list'),
    path('playlists/', views.Playlist.as_view(), name='playlists'),
    path('playlists/new', views.Playlist_Create.as_view(), name='playlist-create'),
]
