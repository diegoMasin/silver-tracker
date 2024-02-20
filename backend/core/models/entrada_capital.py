from datetime import datetime

from django.db import models


class EntradaCapital(models.Model):
    TIPO_ENTRADA_CHOICES = [
        ('aporte_financeiro', 'Aporte Financeiro'),
        ('emprestimo', 'Empréstimo'),
    ]

    TIPO_INVESTIMENTO_CHOICES = [
        ('proprio', 'Próprio'),
        ('terceiros', 'Terceiros'),
    ]

    tipo_entrada = models.CharField(
        max_length=20, choices=TIPO_ENTRADA_CHOICES)
    tipo_investimento = models.CharField(
        max_length=20, choices=TIPO_INVESTIMENTO_CHOICES)
    detalhes = models.TextField(blank=True, null=True)
    valor_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrada = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'entrada_capital'

    def __str__(self):
        return f"{self.tipo_entrada} - {self.valor_entrada}"

    def save(self, *args, **kwargs):
        if not self.data_entrada:
            self.data_entrada = datetime.now()
