from django import forms
from workouts.models import WorkoutExercise, WorkoutPlan

class WorkoutPlanForms(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['athlete','name','description','start_date','end_date','status',]

        widgets = {
            'athlete': forms.Select(attrs={
                'class': 'form-select',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Treino A - Hipertrofia',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descreva os objetivos ou observações da ficha...',
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
        }

        labels = {
            'athlete': 'Aluno',
            'name': 'Nome da ficha',
            'description': 'Descrição',
            'start_date': 'Data de início',
            'end_date': 'Data de término',
            'status': 'Status',
        }




class WorkoutExerciseForms(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise','order','sets','repetitions','weight_kg','rest_seconds','notes',]

        widgets = {
            'exercise': forms.Select(attrs={
                'class': 'form-select'
            }),

            'order': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'sets': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'repetitions': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: 12 ou 10-12'
            }),

            'weight_kg': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Ex.: 20.00'
            }),

            'rest_seconds': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observações sobre o exercício'
            }),
        }



        labels = {
            'exercise': 'Exercício',
            'order': 'Ordem na ficha',
            'sets': 'Séries',
            'repetitions': 'Repetições',
            'weight_kg': 'Peso (kg)',
            'rest_seconds': 'Descanso (segundos)',
            'notes': 'Observações',
        }
