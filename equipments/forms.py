from django import forms
from .models import Equipment


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment

        fields = ['title','brand','category','description','quantity','active','condition',]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do equipamento'
            }),

            'brand': forms.Select(attrs={
                'class': 'form-select'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva o equipamento...'
            }),

            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),

            'active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),

            'condition': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

        labels = {
            'title': 'Nome do equipamento',
            'brand': 'Marca',
            'category': 'Categoria',
            'description': 'Descrição',
            'quantity': 'Quantidade',
            'active': 'Equipamento ativo',
            'condition': 'Condição do equipamento',
        }