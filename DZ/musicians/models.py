from django.db import models

# Create your models here.
from django.db import models


class Musician(models.Model):
    Musician_id = models.AutoField(primary_key=True)
    Musician_name = models.CharField(max_length=100)
    Site = models.CharField(max_length=200)

class Song(models.Model):
    Song_id = models.AutoField(primary_key=True)
    Musician_key = models.ForeignKey(Musician, on_delete=models.CASCADE)
    slug = models.SlugField(default=1)
    Song_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    img = models.CharField(max_length=100)


