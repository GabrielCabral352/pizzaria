from django.db import models


class Cardapio(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'cardapio'

    def __str__(self):
        return self.descricao


class Produto(models.Model):
    nome = models.CharField(max_length=20)
    estoque = models.IntegerField()

    class Meta:
        db_table = 'Produto'

    def __str__(self):
        return self.nome


class Items(models.Model):
    quantidade = models.IntegerField()
    id_card = models.ForeignKey(Cardapio, on_delete=models.CASCADE, verbose_name='Sabor')
    id_prod = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Ingredientes')

    class Meta:
        db_table = 'Items'

    def __str__(self):
        return str(self.id)

