from django.contrib import admin
from cardapio.models import Cardapio, Items, Produto
from home.models import Cliente, Sub_pedido, Pedido

admin.site.register(Cardapio)
admin.site.register(Items)
admin.site.register(Produto)