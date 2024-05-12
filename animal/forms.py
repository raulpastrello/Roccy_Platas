from django.forms.models import BaseInlineFormSet
from django.forms import ModelForm
from django import forms
from animal.models import Dono
from animal.models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
           'nome', 'dono', 'raca_pet', 'sexo', 'categoria_pet', 'cor_pet', 'altura', 'peso', 'vacinas_pet', 'motivo_entrada_pet', 'tipo_entrega', 'imagem', 'slug'
        ]
        

class DonoForm(forms.ModelForm):
    class Meta:
        model = Dono
        fields = [
           'dono', 'contato', 'CPF'
        ]
        

