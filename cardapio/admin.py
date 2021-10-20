from django.contrib import admin
from cardapio.models import Cardapio, Item, Produto


class itemsAdmin(admin.ModelAdmin):
    list_display = ('id_card', 'id_prod', 'quantidade')
    list_filter = ('id_card',)


class cardAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor')
    list_filter = ('tipo', )


class prodAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estoque')


admin.site.register(Cardapio, cardAdmin)
admin.site.register(Item, itemsAdmin)
admin.site.register(Produto, prodAdmin)