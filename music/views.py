from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album, song , cart
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm, LoginForm
from django.views.generic import View
from .forms import SongForm
from django.db import IntegrityError
from .models import product as Product


def CreateSong(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            file_type = form.cleaned_data['file_type']
            title = form.cleaned_data['title']
            stars = form.cleaned_data['stars']
            favourite = form.cleaned_data['favourite']
            newsong = song()
            newsong.album_id = album.id
            newsong.file_type = file_type
            newsong.title = title
            newsong.stars = stars
            newsong.is_fav = favourite
            newsong.save()
            return redirect('music:index')
    else:
        form = SongForm()
    return render(request, 'create_song.html', {'form': form, 'album': album})


def addtocart(request,product_id):
   prod = Product.objects.get(id=product_id)
   try:
      ncart = cart.objects.get(user=request.user)
      ncart.products.add(prod)
      ncart.save()
   except IntegrityError:
       return render(request, 'index.html', {'noalbum': 'You already have made a Cart', 's_status': 'danger'})
   return render(request,'index.html',{'noalbum':'Added to Cart','s_status':'success'})


def Index(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }
    return render(request, 'index.html', context)

def product_index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_index.html', context)



def album_fav(request, album_id):
    album = Album.objects.get(id=album_id)
    if album.is_fav == True:
        album.is_fav = False
        noalbum = "Album '"+album.album_title + "' UnFavourited."
        s_status = 'danger'
    else:
        album.is_fav = True
        noalbum = "Album '"+album.album_title + "' Favourited."
        s_status = 'success'
    album.save()
    return render(request, 'index.html', {'albums': Album.objects.all(), 'noalbum': noalbum, 's_status': s_status})


def album_details(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
        context = {
            'album': album
        }
    except Album.DoesNotExist:
        return render(request, '404.html', {'album_id': album_id})
    return render(request, 'details.html', context)


def product_details(request, product_slug,product_id):
    try:
        product = get_object_or_404(Product,id=product_id)
        context = {
            'product': product
        }
    except Product.DoesNotExist:
        return render(request, '404.html', {'product_id': product_id})
    return render(request, 'product_details.html', context)




def fav(request, album_id):
    album = Album.objects.get(id=album_id)
    song_id = request.POST['song']
    songsel = get_object_or_404(song, id=song_id)
    if(songsel.is_fav == True):
        error_message = " '" + songsel.title + "' " + " is UnFavourited"
        error_type = "danger"
        songsel.is_fav = False
    else:
        songsel.is_fav = True
        error_message = " '" + songsel.title + "' is Favourited"
        error_type = "success"
    songsel.save()
    return render(request, 'details.html', {'album': album, 'mesg': error_message, 'mesg_status': error_type})


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
    if(request.POST and request.POST['artist'] and request.POST['title'] and request.POST['genre'] and request.FILES['album_logo']):
        album = Album()
        album.artist = request.POST['artist']
        album.album_title = request.POST['title']
        album.genre = request.POST['genre']
        album.album_logo = request.FILES['album_logo']
        album.save()
        mesg = "Album created successfully"
        mesg_status = "success"
        return render(request, 'details.html', {'album': album, 'mesg': mesg, 'mesg_status': mesg_status})
    else:
        mesg = "Fill the form carefully , all fields are mandatory"
        mesg_status = "danger"
    return render(request, 'create_album.html', {'mesg': mesg, 'mesg_status': mesg_status})


def update_album(request, album_id):
    album = Album.objects.get(id=album_id)
    mesg_status = "warning"
    mesg = "hello"
    if(request.POST and request.POST['artist'] and request.POST['title'] and request.POST['genre'] and request.FILES['album_logo']):
        album.artist = request.POST['artist']
        album.album_title = request.POST['title']
        album.genre = request.POST['genre']
        album.album_logo = request.FILES['album_logo']
        album.save()
        mesg = " Album updated successfully"
        mesg_status = "success"
        return render(request, 'details.html', {'album': album, 'mesg': mesg, 'mesg_status': mesg_status})
    return render(request, 'update_album.html', {'mesg': mesg, 'mesg_status': mesg_status, 'album': album})


def delete_album(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    albums = Album.objects.all()
    noalbum = "Album Deleted"
    s_status = "danger"
    return redirect('/music')


def Login(request):
    if(request.POST):
        form = LoginForm(request.POST)
        error = ""
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('music:index')
            else:
                error = "Invalid Username or Password , Try Again with correct credentials."
    else:
        error = ""
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error': error})


class UserFormView(View):
    form_class = UserForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})


def profile(request):
    return render(request, 'profile.html')


def user_logout(request):
    logout(request)
    return redirect('music:index')
