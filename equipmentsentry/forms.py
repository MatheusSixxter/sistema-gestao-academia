from django import forms
from equipmentsentry.models import EquipmentEntry



class EquipmentEntryForm(forms.ModelForm):

    #Deixei fora pra colocar um decimal field e tratar melhor.
    total_value = forms.DecimalField(
         label='Valor total da entrada',
         max_digits=12,
         decimal_places=2,
         min_value=0.01,
         widget=forms.NumberInput(attrs={
             'class': 'form-control',
              'placeholder': 'Ex: 1500.00',
             'step': '0.01',
             'min': '0'
         })
     )




    class Meta:
        model = EquipmentEntry
        fields = ['purchase_date', 'equipment', 'supplier', 'quantity', 'total_value',]

        

        widgets = {

            'purchase_date': forms.DateInput(attrs={'class':'form-control',
                                                     'type': 'date'}),


            'equipment': forms.Select(attrs={'class': 
                                             'form-select'}),


            'supplier': forms.Select(attrs={'class': 
                                            'form-select'}),


            'quantity': forms.NumberInput(attrs={'class': 
                                                 'form-control'}),

        }



        labels = {
            'purchase_date': 'Data de compra',
            'equipment': 'Equipamento',
            'supplier': 'Fornecedor(a)',
            'quantity': 'Quantidade',
         
        
        }




