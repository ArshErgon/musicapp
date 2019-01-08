from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album, song


def index(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }
    return render(request, 'index.html', context)


def album_details(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
        context = {
            'album': album
        }
    except Album.DoesNotExist:
        return render(request, '404.html', {'album_id': album_id})
    return render(request, 'details.html', context)
