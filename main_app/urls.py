from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('songs/', views.SongList.as_view(), name='song-list'),
    path('playlists/', views.Playlist_View.as_view(), name='playlists'),
    path('playlists/new', views.Playlist_Create.as_view(), name='playlist-create'),
    path('user/<username>/', views.profile, name='profile'),
    path('playlists/<int:pk>/', views.Playlist_Detail.as_view(), name='playlist-detail'),
    path('playlists/<int:pk>/update', views.Playlist_Update.as_view(), name='playlist-update'),
    path('playlists/<int:pk>/delete', views.Playlist_Delete.as_view(), name='playlist-delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
