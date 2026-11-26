from django import forms
from exercises.models import Exercise


class ExerciseForm(forms.ModelForm):
   
    CATEGORY_CHOICES = [
    ('chest', 'Peito'),
    ('back', 'Costas'),
    ('shoulders', 'Ombros'),
    ('biceps', 'Bíceps'),
    ('triceps', 'Tríceps'),
    ('forearms', 'Antebraços'),
    ('legs', 'Pernas'),
    ('glutes', 'Glúteos'),
    ('calves', 'Panturrilhas'),
    ('abs', 'Abdômen'),
    ('obliques', 'Oblíquos'),
    ('lower_back', 'Lombar'),
    ('full_body', 'Corpo inteiro'),
    ('cardio', 'Cardio'),
    ('mobility', 'Mobilidade e alongamento'),
    ('functional', 'Treinamento funcional'),
    ]

            
    MUSCLE_GROUP_CHOICES = [
    # Peito
    ('pectoralis_major', 'Peitoral maior'),
    ('pectoralis_minor', 'Peitoral menor'),

    # Costas
    ('latissimus_dorsi', 'Latíssimo do dorso'),
    ('trapezius', 'Trapézio'),
    ('rhomboids', 'Romboides'),
    ('teres_major', 'Redondo maior'),
    ('erector_spinae', 'Eretores da espinha'),

    # Ombros
    ('anterior_deltoid', 'Deltoide anterior'),
    ('lateral_deltoid', 'Deltoide lateral'),
    ('posterior_deltoid', 'Deltoide posterior'),
    ('rotator_cuff', 'Manguito rotador'),

    # Braços e antebraços
    ('biceps_brachii', 'Bíceps braquial'),
    ('brachialis', 'Braquial'),
    ('triceps_brachii', 'Tríceps braquial'),
    ('forearm_muscles', 'Músculos do antebraço'),

    # Pernas
    ('quadriceps', 'Quadríceps'),
    ('hamstrings', 'Posteriores da coxa'),
    ('adductors', 'Adutores'),
    ('abductors', 'Abdutores'),
    ('gluteus_maximus', 'Glúteo máximo'),
    ('gluteus_medius', 'Glúteo médio'),
    ('gluteus_minimus', 'Glúteo mínimo'),
    ('gastrocnemius', 'Gastrocnêmio'),
    ('soleus', 'Sóleo'),
    ('tibialis_anterior', 'Tibial anterior'),

    # Abdômen e região central
    ('rectus_abdominis', 'Reto abdominal'),
    ('external_obliques', 'Oblíquos externos'),
    ('internal_obliques', 'Oblíquos internos'),
    ('transverse_abdominis', 'Transverso do abdômen'),
    ('hip_flexors', 'Flexores do quadril'),

    # Outros
    ('hip_adductors', 'Adutores do quadril'),
    ('hip_abductors', 'Abdutores do quadril'),
    ('full_body_muscles', 'Múltiplos grupos musculares'),
]


    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 
                                     'form-control'})

    )

    muscle_group = forms.ChoiceField(
        choices=MUSCLE_GROUP_CHOICES,
        widget=forms.Select(attrs={'class': 
                                     'form-control'})
)
    


    class Meta:
        model = Exercise
        fields = ['name', 'category', 'muscle_group', 'equipament', ]


        widgets = {

            'name': forms.TextInput(attrs={'class': 
                                     'form-control'}),

         

            'equipament': forms.Select(attrs={'class': 
                                     'form-select'}),

        }


        labels = {

            'name': 'Nome',
            'category': 'Categoria ',
            'muscle_group': 'Músculo Principal',
            'equipament': 'Equipamento de realização',
            
        }