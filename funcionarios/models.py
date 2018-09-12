from django.db import models

class Funcionario(models.Model):
    #O ID é criado automaticamente pelo banco de dados.

    nome = models.CharField(max_length=150)
    idade = models.IntegerField()
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
