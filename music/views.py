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


def fav(request, song_id):
    songsel = get_object_or_404(song, id=song_id)
    if(songsel.is_fav):
        songsel.is_fav = False
    else:
        songsel.is_fav = True
    error_message = "Song Favourited"
    error_type = "success"
    return render(request, 'details.html', {'error_message': error_message, 'error_type': error_type})


def search(request):
    sparam = request.POST['search']
    album_count = Album.objects.filter(album_title__contains=sparam).count()
    albums = Album.objects.filter(album_title__contains=sparam)
    noalbum = " There are " + str(album_count) + \
        " albums for your search '"+sparam + "' "
    s_status = 'success'
    if(not (albums)):
        s_status = 'danger'
        noalbum = 'No albums Found for your search "'+sparam + '"'
    return render(request, 'index.html', {'noalbum': noalbum, 's_status': s_status, 'albums': albums})


def create_album(request):
    mesg_status = "warning"
    if(request.POST['artist'] and request.POST['title'] and request.POST['genre'] and request.FILES['album_logo']):
        album = Album()
        album.artist = request.POST['artist']
        album.album_title = request.POST['title']
        album.genre = request.POST['genre']
        album.album_logo = request.FILES['album_logo']
        album.save()
        mesg = " Album created successfully"
        mesg_status = "success"
        return render(request, 'details.html', {'album': album, 'mesg': mesg, 'mesg_status': mesg_status})
    else:
        mesg = "Fill the form carefully , all fields are mandatory"
        mesg_status = "danger"
    return render(request, 'create_album.html', {'mesg': mesg, 'mesg_status': mesg_status})


def update_album(request):
    return render(request, 'index.html')


def delete_album(request):
    return render(request, 'index.html')
