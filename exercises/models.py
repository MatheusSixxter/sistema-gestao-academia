from django.db import models
from equipments.models import Equipment


class Exercise(models.Model):

    name = models.CharField(max_length=100, unique=True)

    category = models.CharField(max_length=50, blank=True, null=True)

    muscle_group = models.CharField(max_length=100, blank=True, null=True)

    equipament = models.ForeignKey(Equipment,
                                    on_delete=models.PROTECT,
                                      related_name='exercises')
       
    description = models.TextField(blank=True,null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['name']
    

    def __str__(self):
        return self.name
