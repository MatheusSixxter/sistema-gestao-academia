from django.db import models
from equipments.models import Equipment
from suppliers.models import Supplier

class EquipmentEntry(models.Model):

    equipment = models.ForeignKey(Equipment,
                                  on_delete=models.PROTECT,
                                    related_name='entries')

    supplier = models.ForeignKey(Supplier,
                                  on_delete=models.PROTECT,
                                    related_name='entries')

    quantity = models.PositiveIntegerField(default=0)

    total_value = models.DecimalField(
        max_digits=12, 
        decimal_places=2)


    purchase_date = models.DateField()

    
    created_at = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-created_at']



    def __str__(self):
         return f'{self.equipment} - {self.quantity} unidades'






