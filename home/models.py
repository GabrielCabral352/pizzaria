from django.db import models
from cardapio.models import Cardapio


class Cliente(models.Model):
    nome = models.CharField(max_length=20)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nome


class Sub_pedido(models.Model):
    id_card = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    class Meta:
        db_table = 'carrinho'


class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_subp = models.ForeignKey(Sub_pedido, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Pedido'
