from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class GeoHistory(models.Model):
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    author = models.TextField()