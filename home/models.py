from django.db import models
from cardapio.models import Cardapio


class Cliente(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Sub_pedido(models.Model):
    id = models.IntegerField(max_length=5, primary_key=True, unique=False)
    id_card = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_subp = models.ForeignKey(Sub_pedido, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_cliente)