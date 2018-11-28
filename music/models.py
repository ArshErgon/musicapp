from django.db import models

# Create your models here.

class Album(models.Model):
   artist = models.CharField(max_length=50)
   album_title = models.CharField(max_length=100)
   genre = models.CharField(max_length=50)
   album_logo = models.CharField(max_length=200)

   def __str__(self):
      return self.artist +" | " + self.album_title + " | " + self.genre 


class song(models.Model):
   album = models.ForeignKey(Album , on_delete=models.CASCADE)
   file_type = models.CharField(max_length=10)
   title = models.CharField(max_length=50)
   stars = models.IntegerField(max_length=5)

   def __str__(self):
         return self.title + ' | ' + str(self.album) + ' | ' + str(self.stars) + ' | ' + self.file_type