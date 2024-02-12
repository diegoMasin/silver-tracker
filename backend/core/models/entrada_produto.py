from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models

from .pessoa import Pessoa
from .produto import Produto


class EntradaProduto(models.Model):
    TIPO_MOVIMENTO_CHOICES = [
        ('compra', 'Compra'),
        ('ajuste', 'Ajuste de Inventário'),
        ('devolucao', 'Devolução'),
    ]

    codigo_entrada = models.CharField(max_length=50)
    tipo_movimento = models.CharField(
        max_length=20, choices=TIPO_MOVIMENTO_CHOICES)
    nf = models.PositiveIntegerField(blank=True, null=True)
    fornecedor = models.ForeignKey(
        Pessoa, blank=True, null=True, on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'fornecedor'})
    observacao = models.TextField(blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def save(self, *args, **kwargs):
        # Gera o código da entrada automaticamente
        if not self.codigo_entrada:
            tipo_inicial = str(self.tipo_movimento)[0].upper()
            data_atual = datetime.now()
            mes_ano_atual = data_atual.strftime('%m%Y')
            self.codigo_entrada = f"{tipo_inicial}{mes_ano_atual} - {self.produto.codigo}"

        # Atualiza o saldo_estoque do produto
        if self.produto:
            self.produto.atualizar_saldo_estoque(self.quantidade)

        if not self.fornecedor and self.tipo_movimento == 'compra':
            raise ValidationError(
                "O fornecedor é obrigatório para entradas do tipo 'compra'.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo_entrada} - {self.produto.nome_produto}"

    class Meta:
        db_table = 'entrada_produto'
