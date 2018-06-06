from django.db import models
from django.utils import timezone


class Venda(models.Model):
    data = models.DateTimeField(default=timezone.now)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def adicionar(self):
        self.data = timezone.now().date()
        self.save()

    def __str__(self):
        return self.descricao
