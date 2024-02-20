from datetime import datetime

from django.db import models


class Despesa(models.Model):
    TIPO_DESPESA_CHOICES = [
        ('compra_produtos', 'Compra de Produtos'),
        ('compra_suprimentos', 'Compra de Suprimentos'),
        ('pagamento_conta', 'Pagamento de Conta'),
        ('prolabore', 'Pró-labore'),
        ('outras_retiradas', 'Outras Retiradas'),
    ]

    tipo_despesa = models.CharField(
        max_length=20, choices=TIPO_DESPESA_CHOICES)
    detalhes = models.TextField(blank=True, null=True)
    valor_despesa = models.DecimalField(max_digits=10, decimal_places=2)
    data_despesa = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.data_despesa:
            self.data_despesa = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo_despesa} - {self.valor_despesa}"

    class Meta:
        db_table = 'despesa'
