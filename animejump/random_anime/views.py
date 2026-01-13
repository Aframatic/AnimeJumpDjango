from django.shortcuts import render
from main.models import Anime


def index(request):
    anime = Anime.objects.filter(published=True).order_by('?').first()
    return render(request, 'main/anime_detail.html', {'anime': anime})