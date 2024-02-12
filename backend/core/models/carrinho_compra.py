from datetime import datetime
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .pessoa import Pessoa
from .produto import Produto


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(
        'CarrinhoCompra', related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    total_parcial = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # if self.quantidade > self.produto.saldo_estoque:
        #     raise ValueError("A quantidade é superior ao estoque no momento!")
        self.total_parcial = self.produto.preco_venda * self.quantidade
        if self.pk:
            old_item = ItemCarrinho.objects.get(pk=self.pk)
            diferenca_quantidade = old_item.quantidade - self.quantidade
            self.produto.atualizar_saldo_estoque(diferenca_quantidade)
            self.carrinho.atualizar_total(old_item.total_parcial * -1)
        else:
            self.produto.atualizar_saldo_estoque(self.quantidade * -1)
        self.carrinho.atualizar_total(self.total_parcial)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto} - {self.quantidade}"

    class Meta:
        db_table = 'item_carrinho'


@receiver(pre_delete, sender=ItemCarrinho)
def excluir_item_carrinho(sender, instance, **kwargs):
    instance.carrinho.atualizar_total(instance.total_parcial * -1)
    instance.produto.atualizar_saldo_estoque(instance.quantidade)


class CarrinhoCompra(models.Model):
    TIPO_CHOICES = [
        ('pix', 'Pix'),
        ('debito', 'Débito'),
        ('credito', 'Crédito'),
        ('dinheiro', 'Dinheiro'),
    ]

    cliente = models.ForeignKey(
        Pessoa, on_delete=models.CASCADE, limit_choices_to={'tipo': 'cliente'})
    desconto = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    forma_pagamento = models.CharField(max_length=20, choices=TIPO_CHOICES)
    desconto_maquina = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    total_pago = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])

    def __str__(self):
        data_atual = datetime.now().strftime('%d/%m/%Y')
        return f"Carrinho de {self.cliente} - {data_atual}"

    def save(self, *args, **kwargs):
        # Atualiza o total pago ao salvar (no futuro incluir o cálculo do desconto da maquina)
        # total pago sempre significará o valor real exato recebido na conta (ou carteira)
        self.total_pago = Decimal(str(self.total)) - \
            Decimal(str(self.desconto))
        if self.total_pago < 0:
            raise ValueError("O total a ser pago não pode ser negativo.")
        super().save(*args, **kwargs)

    def atualizar_total(self, valor: Decimal):
        valor_decimal = Decimal(str(valor))
        total = Decimal(str(self.total))
        self.total = total + valor_decimal
        self.save()

    class Meta:
        db_table = 'carrinho_compra'
