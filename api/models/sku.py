from django.db import models

from api.models import Car


class Sku(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    year = models.CharField()
    color = models.CharField()

    def __str__(self):
        return f'{self.car} ({self.year}) - {self.price}'

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural= 'Автомобили'
