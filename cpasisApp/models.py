from django.db import models

# Create your models here.
class Eixo(models.Model):
    id_eixo = models.AutoField(primary_key=True)
    nome_eixo=models.CharField(max_length=200, blank= True, null=True, unique=True)

    def __str__(self):
        return self.nome_eixo

class Dimensao(models.Model):
    id_dim = models.AutoField(primary_key = True)
    nome_dim = models.CharField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return self.nome_dim

class Indicador(models.Model):
    id_indicador =models.AutoField(primary_key=True)
    id_eixo = models.ForeignKey(Eixo, models.DO_NOTHING, db_column='id_eixo', blank=True, null=True)
    id_dim = models.ForeignKey(Dimensao, models.DO_NOTHING, db_column='id_dim', blank=True, null=True)
    nome_indicador = models.CharField(max_length=200, blank=True, null=True, unique=True)
    nota_indicador = models.CharField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return self.nome_indicador
