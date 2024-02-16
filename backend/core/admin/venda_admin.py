from django.contrib import admin

from ..models.venda import ItemVenda, Venda


class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1  # Permite adicionar vários itens por vez
    readonly_fields = ['total_parcial']


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'forma_pagamento',
                    'desconto_maquina', 'total', 'desconto', 'total_pago', 'foi_pago', 'data_cadastro']
    list_filter = ['forma_pagamento', 'foi_pago']
    earch_fields = ['cliente__nome', 'total', 'total_pago']
    inlines = [ItemVendaInline]
    readonly_fields = ['total', 'total_pago']
    fieldsets = (
        ('Detalhes da Venda', {
            'fields': ('cliente', 'forma_pagamento', 'data_cadastro', 'desconto',
                       'desconto_maquina', 'total', 'total_pago', 'foi_pago')
        }),
    )
