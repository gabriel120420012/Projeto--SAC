from django import forms
from cpasisApp.models import Eixo,Indicador,Dimensao

class EixoForm(forms.ModelForm):
    class Meta:
        model = Eixo
        fields = '__all__'


class DimensaoForm(forms.ModelForm):
    class Meta:
        model = Dimensao
        fields = '__all__'

class IndicadorForm(forms.ModelForm):
    class Meta:
        model=Indicador
        #fields = '__all__'
        fields = ['id_indicador' ,'nome_indicador','id_eixo','id_dim']