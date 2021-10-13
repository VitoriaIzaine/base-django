from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    datainicio = models.DateTimeField(default=timezone.now)
    mostrar = models.BooleanField(default=True)
    #categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING())
    def __str__(self):
        return self.titulo


