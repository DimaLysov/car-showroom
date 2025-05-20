from django.db import models
from django.utils import timezone

from api.models import Client, Manager, Sku


class Contract(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'наличкой'),
        ('card', 'картой'),
        ('crypt', 'криптой')
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHODS, default='cash')

    def __str__(self):
        return f'{self.client} - {self.manager} ({self.date})'