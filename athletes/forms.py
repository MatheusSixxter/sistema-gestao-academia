from django import forms
from athletes.models import Athlete

class AthleteForm(forms.ModelForm):

    class Meta:
        model = Athlete
        fields = ['name', 'email', 'cpf', 'phone', 'plan', 'status',]

        widgets = {

            'name': forms.TextInput(attrs={'class': 
                                     'form-control'}),

            'email': forms.EmailInput(attrs={'class':
                                              'form-control'}),

            'cpf': forms.TextInput(attrs={'class': 
                                     'form-control'}),

            'phone': forms.TextInput(attrs={'class': 
                                     'form-control'}),


            'plan': forms.Select(attrs={'class': 
                                     'form-select'}),


            'status': forms.Select(attrs={'class': 
                                     'form-select'}),

        }

        labels = {

            'name': 'Nome',
            'email': 'Email',
            'cpf': 'CPF',
            'phone': 'Telefone',
            'plan': 'Plano atual',
            'status': 'Status atual',
        }

