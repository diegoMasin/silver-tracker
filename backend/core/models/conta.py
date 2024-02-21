from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import models

from .despesa import Despesa
from .entrada_capital import EntradaCapital
from .venda import Venda


class Conta(models.Model):
    nome_conta = models.CharField(max_length=255, unique=True)
    total_investido = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    total_gastos = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    total_vendido = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    lucro_total = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    lucro_livre = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    investimento_amortizado = models.BooleanField(default=False)
    parcial_conta = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def clean(self):
        # Verifica se já existe uma conta criada
        if Conta.objects.exists() and not self.pk:
            raise ValidationError(
                'Já existe uma conta registrada. Apenas uma conta é permitida.')

    def save(self, *args, **kwargs):
        # Calcula as informações dos campos
        self.total_investido = self.calcular_total_investido()
        self.total_gastos = self.calcular_total_gastos()
        self.total_vendido = self.calcular_total_vendido()
        self.lucro_total = self.calcular_lucro_total()
        self.lucro_livre = self.calcular_lucro_livre()
        self.investimento_amortizado = self.calcular_investimento_amortizado()
        self.parcial_conta = self.calcular_parcial_conta()

        super().save(*args, **kwargs)

    def calcular_total_investido(self):
        total_investimentos = EntradaCapital.objects.aggregate(
            models.Sum('valor_entrada'))['valor_entrada__sum']
        return total_investimentos if total_investimentos is not None else 0.0

    def calcular_total_gastos(self):
        total_gastos = Despesa.objects.aggregate(
            models.Sum('valor_despesa'))['valor_despesa__sum']
        return total_gastos if total_gastos is not None else 0.0

    def calcular_total_vendido(self):
        total_vendido = Venda.objects.filter(foi_pago=True).aggregate(
            models.Sum('total_pago'))['total_pago__sum']
        return total_vendido if total_vendido is not None else 0.0

    def calcular_lucro_total(self):
        return Decimal(str(self.total_vendido)) - Decimal(str(self.total_gastos))

    def calcular_lucro_livre(self):
        return Decimal(str(self.lucro_total)) - Decimal(str(self.total_investido))

    def calcular_investimento_amortizado(self):
        lucro_livre = self.calcular_lucro_livre()
        return lucro_livre >= Decimal('0.00')

    def calcular_parcial_conta(self):
        total_investido = Decimal(str(self.total_investido))
        total_gastos = Decimal(str(self.total_gastos))
        total_vendido = Decimal(str(self.total_vendido))
        return total_investido - total_gastos + total_vendido

    def __str__(self):
        return f"{self.nome_conta}"

    class Meta:
        db_table = 'conta'
