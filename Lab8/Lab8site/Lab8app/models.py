from django.db import models
class Song(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	duration=models.CharField(max_length=50)
	img=models.CharField(max_length=100)
# Create your models here.
