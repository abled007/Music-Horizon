from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Song


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class SongList(TemplateView):
       template_name = 'songlist.html'

  