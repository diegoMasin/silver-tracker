from django.contrib import admin

from .models.carrinho_compra import CarrinhoCompra, ItemCarrinho
from .models.entrada_produto import EntradaProduto
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


@admin.register(EntradaProduto)
class EntradaProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo_entrada', 'tipo_movimento',
                    'nf', 'fornecedor', 'produto', 'quantidade']
    list_filter = ['tipo_movimento', 'fornecedor', 'produto']
    search_fields = ['codigo_entrada', 'nf',
                     'fornecedor__nome', 'produto__nome_produto']
    readonly_fields = ['codigo_entrada']


# @admin.register(ItemCarrinho)
class ItemCarrinhoInline(admin.TabularInline):
    model = ItemCarrinho
    extra = 1  # Permite adicionar vários itens por vez
    readonly_fields = ['total_parcial']


@admin.register(CarrinhoCompra)
class CarrinhoCompraAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'total', 'desconto']
    inlines = [ItemCarrinhoInline]
    readonly_fields = ['total']
