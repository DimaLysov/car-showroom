from django.db import models
from django.utils import timezone


class Manager(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    sold_cars = models.IntegerField()
    date_employment = models.DateTimeField(default=timezone.now)
    salary = models.BigIntegerField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'менеджера'
        verbose_name_plural= 'Менеджеры'