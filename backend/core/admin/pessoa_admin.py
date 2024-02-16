from django.contrib import admin

from ..models.pessoa import Pessoa


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
