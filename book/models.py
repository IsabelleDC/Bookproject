from django.contrib.auth.models import AbstractUser
from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.


class Visitor(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_picture', blank=True, null=True)
    position = GeopositionField()


class Genre(models.Model):
    name = models. CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(Visitor, related_name='genres')

    def __unicode__(self):
        return self.name


class Livre(models.Model):
    name = models. CharField(max_length=50)
    author = models.TextField(max_length=30, null=True, blank=True)
    # streetnum = models.IntegerField(null=True, blank=True)
    # street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    zipcode = models.IntegerField(max_length=10, null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='livres')
    image = models.ImageField(upload_to='livre_image', blank=True, null=True)

    def __unicode__(self):
        return self.name

