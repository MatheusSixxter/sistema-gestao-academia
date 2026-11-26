from django.db import models
from brands.models import Brand




CATEGORY_CHOICES = [
    ('machine', 'Máquina'),
    ('free_weight', 'Peso livre'),
    ('accessory', 'Acessório'),
    ('cardio', 'Cardio'),
    ('other', 'Outro')
]



CONDITION_CHOICES = [

    ('new', 'Novo'),
    ('excellent', 'Excelente'),
    ('good', 'Bom'),
    ('regular', 'Regular'),
    ('bad', 'Ruim'),
    ('damaged', 'Danificado'),
]



class Equipment(models.Model):
    title = models.CharField(max_length=300)

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='equipments')

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='other'

    )

    description = models.TextField(blank=True, null=True)

    quantity = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    condition = models.CharField(
        max_length=30,
        choices=CONDITION_CHOICES,
        default='good'
        
        )

    class Meta:
        ordering = ['title']



    def __str__(self):
        return self.title



                                
