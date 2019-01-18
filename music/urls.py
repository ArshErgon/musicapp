from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.Index, name="index"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^products/$', views.product_index, name="product_index"),
    url(r'^cs/(?P<album_id>[0-9]+)/$', views.CreateSong, name='create_song'),
    url(r'^addtocart/(?P<product_id>[0-9]+)/$',
        views.addtocart, name='addtocart'),
    url(r'^register/$', views.UserFormView.as_view(), name="register"),
    url(r'^login/$', views.Login, name="login"),
    url(r'^(?P<album_id>[0-9]+)/$', views.album_details, name="album_details"),
    url(r'^product/(?P<product_slug>\w+)-(?P<product_id>[0-9]+)/$', views.product_details, name="product_details"),
    url(r'^(?P<album_id>[0-9]+)/fav$',
        views.fav, name="fav"),
    url(r'^(?P<album_id>[0-9]+)/Afav$',
        views.album_fav, name="album_fav"),
    url(r'^search/', views.search, name="search"),
    url(r'^createA/$', views.create_album, name='create_album'),
    url(r'^updateA/(?P<album_id>[0-9]+)/$',
        views.update_album, name='update_album'),
    url(r'^deleteA/(?P<album_id>[0-9]+)/$',
        views.delete_album, name='delete_album'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', views.user_logout, name='logout'),

]
