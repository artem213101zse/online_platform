from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class GeoHistory(models.Model):
    date = models.DateTimeField(verbose_name="Дата")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    accuracy = models.FloatField(verbose_name="Точность")
    altitude = models.FloatField(verbose_name="Высота")
    direction = models.FloatField(verbose_name="Направление")
    speed = models.FloatField(verbose_name="Скорость")
    author = models.TextField(verbose_name="Пользователь")

    class Meta:
        verbose_name = 'Геоданные'
        verbose_name_plural = 'Геоданные'