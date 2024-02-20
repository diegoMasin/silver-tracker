from django.contrib import admin

from ..models.entrada_capital import EntradaCapital


@admin.register(EntradaCapital)
class EntradaCapitalAdmin(admin.ModelAdmin):
    list_display = ['tipo_entrada', 'tipo_investimento',
                    'valor_entrada', 'data_entrada']
    list_filter = ['tipo_entrada', 'tipo_investimento']
    search_fields = ['valor_entrada', 'detalhes']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('tipo_entrada', 'tipo_investimento', 'data_entrada')
        }),
        ('Detalhes da Entrada de Capital', {
            'fields': ('valor_entrada', 'detalhes')
        }),
    )
