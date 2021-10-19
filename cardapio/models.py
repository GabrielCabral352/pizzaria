from django.db import models



class Cardapio(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)



class Cliente(models.Model):
    nome = models.CharField(max_length=20)


class Produto(models.Model):
    nome = models.CharField(max_length=20)
    estoque = models.IntegerField()


class Items(models.Model):
    quantidade = models.IntegerField()
    id_card = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    id_prod = models.ForeignKey(Produto, on_delete=models.CASCADE)


class Sub_pedido(models.Model):
    id_card = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    quantidade = models.IntegerField()


class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_subp = models.ForeignKey(Sub_pedido, on_delete=models.CASCADE)

