from django.db import models

class Produto(models.Model):
    name        = models.CharField     ('name', max_length=100)
    type        = models.CharField     ('type', max_length=20)
    price       = models.DecimalField  ('price', decimal_places=2, max_digits=6)
    stock       = models.IntegerField  ('Quantidade em Estoque')
    
    def __str__(self):
        return self.name

class Cliente(models.Model):
    name        = models.CharField  ('name', max_length=100)
    surname     = models.CharField  ('surname', max_length=100)
    email       = models.EmailField ('email', max_length=50)
