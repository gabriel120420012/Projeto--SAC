from django import forms
from cpasisApp.models import Eixo,Indicador,Dimensao, Curso, Campus, TipoCurso, Publico

class EixoForm(forms.ModelForm):
    class Meta:
        model = Eixo
        #fields = '__all__'
        fields =['nome_eixo']
    nome_eixo = forms.CharField(label='Nome do Eixo')



class DimensaoForm(forms.ModelForm):
    class Meta:
        model = Dimensao
        #fields = '__all__'
        fields = ['nome_dim','id_eixo']
        nome_dim = forms.CharField(label='Nome da Dimensão')

class IndicadorForm(forms.ModelForm):
    class Meta:
        model= Indicador
        fields =['nome_indicador','id_eixo','id_dim', 'nota_indicador', 'id_pub', 'id_curso','id_campus','foto_indicador']
        nome_indicador = forms.CharField(label='Indicador')
        nota_indicador = forms.CharField(label='Nota')

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields =['nome_campus']
        nome_campus = forms.CharField(label='Nome do Campus')

class TipoForm(forms.ModelForm):
    class Meta:
        model = TipoCurso
        fields =['nome_tipo']
        nome_tipo = forms.CharField(label='Nível')


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields =['nome_curso','id_tipo']
        nome_curso = forms.CharField(label='Curso')



class PublicoForm(forms.ModelForm):
    class Meta:
        model = Publico
        fields =['nome_publico','id_campus', 'id_curso']
        nome_publico = forms.CharField(label='Nome do Público')




