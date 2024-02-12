from django.db import models
from django_cpf_cnpj.fields import CNPJField, CPFField


class Pessoa(models.Model):
    TIPO_CHOICES = [
        ('cliente', 'Cliente'),
        ('fornecedor', 'Fornecedor'),
    ]

    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    telefone = models.CharField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cnpj = CNPJField(masked=True, blank=True, null=True)
    cpf = CPFField(masked=True, blank=True, null=True)
    endereco = models.CharField(blank=True, null=True)
    observacoes = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = 'pessoa'
