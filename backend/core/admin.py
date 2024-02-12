from django.contrib import admin

from .models.pessoa import Pessoa
from .models.produto import Produto


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'telefone', 'email',
                    'cnpj', 'cpf', 'endereco', 'observacoes']
    list_filter = ['tipo']
    search_fields = ['nome', 'cnpj', 'cpf', 'email']

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'tipo')
        }),
        ('Contato', {
            'fields': ('telefone', 'email')
        }),
        ('Documentos', {
            'fields': ('cnpj', 'cpf')
        }),
        ('Endereço e Observações', {
            'fields': ('endereco', 'observacoes')
        }),
    )


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome_produto', 'unidade',
                    'preco_custo', 'preco_venda', 'margem', 'saldo_estoque']
    search_fields = ['codigo', 'nome_produto']
    readonly_fields = ['margem', 'saldo_estoque']

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('codigo', 'nome_produto')
        }),
        ('Detalhes do Produto', {
            'fields': ('unidade', 'preco_custo', 'preco_venda', 'margem', 'saldo_estoque')
        }),
    )
