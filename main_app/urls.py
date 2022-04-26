from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('songs/', views.SongList.as_view(), name='song-list'),
    path('playlists/', views.Playlist_View.as_view(), name='playlists'),
    path('playlists/new', views.Playlist_Create.as_view(), name='playlist-create'),
    path('user/<username>/', views.profile, name='profile'),
    path('playlists/<int:pk>/', views.Playlist_Detail.as_view(), name='playlist-detail')
]
