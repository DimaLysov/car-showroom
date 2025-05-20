from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254, unique=True, blank=True, verbose_name="Email адрес")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural= 'Клиенты'