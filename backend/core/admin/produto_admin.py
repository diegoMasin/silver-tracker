from django.contrib import admin

from ..models.produto import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome_produto',
                    'preco_custo', 'preco_venda', 'margem', 'saldo_estoque', 'esta_ativo']
    list_filter = ['tipo', 'esta_ativo']
    search_fields = ['codigo', 'nome_produto', 'preco_venda']
    readonly_fields = ['margem', 'saldo_estoque']

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('codigo', 'nome_produto')
        }),
        ('Detalhes do Produto', {
            'fields': ('tipo', 'unidade', 'saldo_estoque', 'esta_ativo')
        }),
        ('Precificação', {
            'fields': ('preco_custo', 'preco_venda', 'margem')
        }),
    )
