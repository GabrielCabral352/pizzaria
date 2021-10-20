from django.db import models


class Cardapio(models.Model):
    bebida = 'bebida'
    comida = 'comida'

    CHOICES = (
        (bebida, 'bebida'),
        (comida, 'comida'),
    )

    descricao = models.CharField(max_length=50, verbose_name='Nome')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=255, choices=CHOICES)

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


class Item(models.Model):
    id_card = models.ForeignKey(Cardapio, on_delete=models.CASCADE, verbose_name='Receita')
    id_prod = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Ingrediente')
    quantidade = models.IntegerField()

    class Meta:
        db_table = 'Items'

    def __str__(self):
        return str(self.id)