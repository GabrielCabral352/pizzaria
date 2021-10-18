from django.db import models

from django.db import models


class Cardapio(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=8)


class Cliente(models.Model):
    nome = models.CharField(max_length=20)


class Produto(models.Model):
    nome = models.CharField(max_length=20)
    estoque = models.IntegerField(max_digits=10)


class Items(models.Model):
    quantidade = models.IntegerField(max_digits=10)
    id_card = models.ForeignKey(Cardapio, on_delete=models.DO_NOTTING)
    id_prod = models.ForeignKey(Produto, on_delete=models.DO_NOTTING)


class Sub_pedido(models.Model):
    id_card = models.ForeignKey(Cardapio, on_delete=models.DO_NOTTING)
    quantidade = models.IntegerField(max_digits=10)


class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTTING)
    id_subp = models.ForeignKey(Sub_pedido)

