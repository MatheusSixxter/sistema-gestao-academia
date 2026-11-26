from django import forms
import re
from suppliers.models import Supplier


class SupplierForm(forms.ModelForm):


    class Meta:
        model = Supplier
        fields = ['name', 'cnpj', 'phone', 'email',]


        widgets = {

            'name': forms.TextInput(attrs={'class': 
                                     'form-control', 
                                     'placeholder': 'Nome do fornecedor'}),


            'cnpj': forms.TextInput(attrs={'class':
                                           'form-control', 
                                           'placeholder': '00.000.000/0000-00'}),




            'phone': forms.TextInput(attrs={'class': 
                                     'form-control', 
                                     'placeholder': '(00) 00000-0000' }),


            'email': forms.EmailInput(attrs={'class': 
                                     'form-control', 
                                     'placeholder': 'email@exemplo.com'}),

        }



        labels = {

            'name': 'Nome',
            'cnpj': 'CNPJ',
            'phone': 'Telefone',
            'email': 'Email',
            
        }


    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']

    # Remove a máscara e padroniza letras maiúsculas.
        cnpj = re.sub(r'[./\-\s]', '', cnpj).upper()

        return cnpj