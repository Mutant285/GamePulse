import datetime

from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100, null=False, default='Game')
    downloads = models.IntegerField(null=False, default=0)
    genre = models.CharField(max_length=20, null=False, default='Жанр не определён')
    rating = models.IntegerField(null=False, default=0)
    date = models.DateField(null=False)
    platform = models.CharField(max_length=10, default='ПК')
    author = models.CharField(max_length=20, default='Нет' )
    def __str__(self):
        return self.name


