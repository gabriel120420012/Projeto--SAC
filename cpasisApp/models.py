from django.db import models
from PIL import Image

# Create your models here.
class Eixo(models.Model):
    id_eixo = models.AutoField(primary_key=True)
    nome_eixo=models.CharField(max_length=200, blank= True, null=True, unique=True)

    def __str__(self):
        return self.nome_eixo

class Dimensao(models.Model):
    id_dim = models.AutoField(primary_key = True)
    nome_dim = models.CharField(max_length=200, blank=True, null=True, unique=True)
    id_eixo = models.ForeignKey(Eixo, models.DO_NOTHING, db_column='id_eixo', blank=True, null=True)

    def __str__(self):
        return self.nome_dim


class Campus(models.Model):
    id_campus = models.AutoField(primary_key=True)
    nome_campus = models.CharField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return self.nome_campus

class TipoCurso(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nome_tipo = models.CharField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return self.nome_tipo

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nome_curso = models.CharField(max_length=200, blank=True, null=True, unique=True)
    id_tipo = models.ForeignKey(TipoCurso, models.DO_NOTHING, db_column='id_tipo', blank=True, null=True)

    def __str__(self):
        return self.nome_curso


class Publico(models.Model):
    id_publico =  models.AutoField(primary_key=True)
    nome_publico = models.CharField(max_length=200,blank=True, null=True)
    id_campus = models.ForeignKey(Campus, models.DO_NOTHING, db_column='id_campus', blank=True, null=True)
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)

    def __str__(self):
        return self.nome_publico








class Indicador(models.Model):
    id_indicador =models.AutoField(primary_key=True)
    id_eixo = models.ForeignKey(Eixo, models.DO_NOTHING, db_column='id_eixo', blank=True, null=True)
    id_dim = models.ForeignKey(Dimensao, models.DO_NOTHING, db_column='id_dim', blank=True, null=True)
    id_pub = models.ForeignKey(Publico, models.DO_NOTHING, db_column='id_publico', blank=True, null=True)
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    id_campus = models.ForeignKey(Campus, models.DO_NOTHING, db_column='id_campus', blank=True, null=True)
    nome_indicador = models.TextField(max_length=300, blank=True, null=True)
    nota_indicador = models.CharField(max_length=300, blank=True, null=True)
    foto_indicador = models.ImageField(blank=True, null=True)

    def save(self):
        super().save()
        im =Image.open(self.foto_indicador.path)
        novo_tamanho =(40,40)
        im.thumbnail(novo_tamanho)
        im.save(self.foto_indicador.path)


    def foto_url(self):
        if self.foto_indicador and hasattr(self.foto_indicador, 'url'):
            return self.foto_indicador.url
        else:
            return self.nome_indicador

    def __str__(self):
        return self.nome_indicador

