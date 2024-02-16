from django.contrib import admin

from ..models.entrada_produto import EntradaProduto


@admin.register(EntradaProduto)
class EntradaProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo_entrada', 'produto', 'tipo_movimento',
                    'fornecedor', 'quantidade', 'data_cadastro']
    list_filter = ['tipo_movimento', 'fornecedor', 'produto']
    search_fields = ['codigo_entrada', 'nf',
                     'fornecedor__nome', 'produto__nome_produto']
    readonly_fields = ['codigo_entrada']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('codigo_entrada', 'tipo_movimento', 'data_cadastro')
        }),
        ('Detalhes da Entrada de Produto', {
            'fields': ('fornecedor', 'produto', 'nf', 'quantidade', 'observacao')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        # Se o objeto (produto) já existe, torna todos os campos readonly
        if obj:
            return self.readonly_fields + ['quantidade']
        return self.readonly_fields
