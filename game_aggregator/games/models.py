import datetime


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
    title = models.CharField(max_length=100, null=False, default='Game', primary_key=True)
    genre = models.CharField(max_length=20, null=False, default='Genre is not defined')
    date = models.IntegerField(null=False)
    developer = models.CharField(max_length=100, default='Нет')
    publisher = models.CharField(max_length=100, default='Нет')
    description = models.TextField(default='The description is missing')


    def __str__(self):
        return self.name


