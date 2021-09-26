from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class GeoHistory(models.Model):
    date = models.DateTimeField(verbose_name="Дата")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    altitude = models.FloatField(verbose_name="Высота")
    author = models.TextField(verbose_name="Автор")

    class Meta:
        verbose_name = 'Геоданные'
        verbose_name_plural = 'Геоданные'