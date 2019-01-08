from django.db import models
from django.core.validators import MaxValueValidator
from django.core.urlresolvers import reverse

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:details', kwargs={'id': self.id})

    def __str__(self):
        return self.artist + " | " + self.album_title + " | " + self.genre


class song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    stars = models.IntegerField(validators=[MaxValueValidator(5)])
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)+' | ' + self.title + ' | ' + str(self.album) + ' | ' + str(self.stars) + ' | ' + str(self.is_fav) + ' | ' + self.file_type
