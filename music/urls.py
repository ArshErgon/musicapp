from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.Index, name="index"),
    url(r'^(?P<album_id>[0-9]+)/$', views.album_details, name="album_details"),
    url(r'^(?P<album_id>[0-9]+)/fav$', views.fav, name="fav"),
    url(r'^search/', views.search, name="search"),
    url(r'^createA/$', views.create_album, name='create_album'),
    url(r'^updateA/(?P<album_id>[0-9]+)/$',
        views.update_album, name='update_album'),
    url(r'^deleteA/(?P<album_id>[0-9]+)/$',
        views.delete_album, name='delete_album')
]
