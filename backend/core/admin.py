from django.contrib import admin

from .models.carrinho_compra import CarrinhoCompra, ItemCarrinho
from .models.entrada_produto import EntradaProduto
from .models.pessoa import Pessoa
from .models.produto import Produto


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'telefone', 'email',
                    'cnpj', 'cpf']
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
    list_display = ['codigo', 'nome_produto',
                    'preco_custo', 'preco_venda', 'margem', 'saldo_estoque']
    list_filter = ['tipo']
    search_fields = ['codigo', 'nome_produto', 'preco_venda']
    readonly_fields = ['margem', 'saldo_estoque']

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('codigo', 'nome_produto')
        }),
        ('Detalhes do Produto', {
            'fields': ('unidade', 'preco_custo', 'preco_venda', 'margem', 'saldo_estoque')
        }),
    )


@admin.register(EntradaProduto)
class EntradaProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo_entrada', 'produto', 'tipo_movimento',
                    'fornecedor', 'quantidade']
    list_filter = ['tipo_movimento', 'fornecedor', 'produto']
    search_fields = ['codigo_entrada', 'nf',
                     'fornecedor__nome', 'produto__nome_produto']
    readonly_fields = ['codigo_entrada']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('codigo_entrada', 'tipo_movimento')
        }),
        ('Detalhes da Entrada de Produto', {
            'fields': ('fornecedor', 'produto', 'nf', 'quantidade', 'observacao')
        }),
    )


# @admin.register(ItemCarrinho)
class ItemCarrinhoInline(admin.TabularInline):
    model = ItemCarrinho
    extra = 1  # Permite adicionar vários itens por vez
    readonly_fields = ['total_parcial']


@admin.register(CarrinhoCompra)
class CarrinhoCompraAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'forma_pagamento',
                    'desconto_maquina', 'total', 'desconto', 'total_pago']
    list_filter = ['forma_pagamento']
    earch_fields = ['cliente__nome', 'total', 'total_pago']
    inlines = [ItemCarrinhoInline]
    readonly_fields = ['total', 'total_pago']
    fieldsets = (
        ('Detalhes da Venda', {
            'fields': ('cliente', 'forma_pagamento', 'desconto',
                       'desconto_maquina', 'total', 'total_pago')
        })
    )
