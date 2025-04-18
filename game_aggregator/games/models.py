from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100, null=False, default='Game')
    downloads = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name
