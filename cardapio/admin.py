from django.contrib import admin
from cardapio.models import Cardapio, Items, Produto
from home.models import Cliente, Sub_pedido, Pedido


class itemsAdmin(admin.ModelAdmin):
    list_display = ('id_card','id_prod', 'quantidade')
    list_filter = ('id_card', )

# class produtoAdmin(admin.ModelAdmin):
#     list_display = ('')


admin.site.register(Cardapio)
admin.site.register(Items, itemsAdmin)
admin.site.register(Produto)