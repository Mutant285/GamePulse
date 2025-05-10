import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Game(models.Model):
    name = models.CharField(max_length=100, null=False, default='Game')
    downloads = models.IntegerField(null=False, default=0)
    genre = models.CharField(max_length=20, null=False, default='Жанр не определён')
    rating = IntegerRangeField(min_value=1, max_value=5)
    date = models.DateField(null=False)
    platform = models.CharField(max_length=20, default='ПК')
    author = models.CharField(max_length=20, default='Нет' )
    def __str__(self):
        return self.name


