from django.db import models
from django.core.validators import MaxValueValidator
from django.core.urlresolvers import reverse
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=50)
    album_logo = models.FileField()
    is_fav = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('music:details', kwargs={'id': self.id})

    def __str__(self):
        return self.artist + " | " + self.album_title + " | " + self.genre


class song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=50, unique=True)
    stars = models.IntegerField(validators=[MaxValueValidator(5)])
    is_fav = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+' | ' + self.title + ' | ' + str(self.album) + ' | ' + str(self.stars) + ' | ' + str(self.is_fav) + ' | ' + self.file_type



class product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    img = models.FileField(upload_to='products/')
    slug = models.SlugField(db_index=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return str(self.id)+' | '+str(self.slug)+ ' | ' + str(self.name)+ ' | '+ self.description + ' | '+str(self.price)+' | '+str(self.available)+' | '+str(self.stock)

class cart(models.Model):

    user        = models.ForeignKey(User)
    products    = models.ManyToManyField(product)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)