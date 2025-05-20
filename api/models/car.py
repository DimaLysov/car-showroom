from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.brand} {self.model} - {self.count} шт'

    class Meta:
        verbose_name = 'модель автомобиля'
        verbose_name_plural= 'Модели автомобилей'