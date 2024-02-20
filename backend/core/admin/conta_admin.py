from django.contrib import admin

from ..models.conta import Conta


@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    nome_conta = ['nome_conta', 'parcial_conta', 'ultima_atualizacao']
    readonly_fields = ['total_investido', 'total_gastos', 'total_vendido', 'lucro_total',
                       'lucro_livre', 'investimento_amortizado',
                       'parcial_conta', 'ultima_atualizacao']
    fieldsets = (
        ('Informações Editável', {
            'fields': ('nome_conta',)
        }),
        ('Detalhes Calculados', {
            'fields': ('total_investido', 'total_gastos', 'total_vendido', 'lucro_total',
                       'lucro_livre', 'investimento_amortizado',
                       'parcial_conta', 'ultima_atualizacao')
        }),
    )
