from datetime import datetime
from decimal import Decimal

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
        # Atualiza o total parcial ao salvar
        self.total_parcial = self.produto.preco_venda * self.quantidade
        self.carrinho.atualizar_total(self.total_parcial)
        # Atualiza o estoque do produto
        self.produto.atualizar_saldo_estoque(self.quantidade * -1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto} - {self.quantidade}"


@receiver(pre_delete, sender=ItemCarrinho)
def excluir_item_carrinho(sender, instance, **kwargs):
    instance.carrinho.atualizar_total(instance.total_parcial * -1)
    instance.produto.atualizar_saldo_estoque(instance.quantidade)


class CarrinhoCompra(models.Model):
    cliente = models.ForeignKey(
        Pessoa, on_delete=models.CASCADE, limit_choices_to={'tipo': 'cliente'})
    desconto = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        data_atual = datetime.now().strftime('%d/%m/%Y')
        return f"Carrinho de {self.cliente} - {data_atual}"

    def save(self, *args, **kwargs):
        # Atualiza o total parcial ao salvar
        self.total = Decimal(str(self.total)) - Decimal(str(self.desconto))
        super().save(*args, **kwargs)

    def atualizar_total(self, valor: Decimal):
        valor_decimal = Decimal(str(valor))
        total = Decimal(str(self.total))
        self.total = total + valor_decimal
        self.save()
