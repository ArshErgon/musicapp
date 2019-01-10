from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album, song


def Index(request):
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


def fav(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'details.html')


def search(request):
    sparam = request.POST['search']
    noalbum = sparam
    s_status = 'success'
    albums = Album.objects.filter(album_title__contains=sparam)
    if(not (albums)):
        s_status = 'danger'
        noalbum = 'No albums Found '
    return render(request, 'index.html', {'noalbum': noalbum, 's_status': s_status, 'albums': albums})


def create_album(request):
    return render(request, 'index.html')


def update_album(request):
    return render(request, 'index.html')


def delete_album(request):
    return render(request, 'index.html')
