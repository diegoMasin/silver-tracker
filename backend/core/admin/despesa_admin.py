from django.contrib import admin

from ..models.despesa import Despesa


@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ['tipo_despesa', 'valor_despesa', 'data_despesa']
    list_filter = ['tipo_despesa']
    search_fields = ['valor_despesa', 'detalhes']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('tipo_despesa', 'data_despesa')
        }),
        ('Detalhes da Entrada de Capital', {
            'fields': ('valor_despesa', 'detalhes')
        }),
    )
