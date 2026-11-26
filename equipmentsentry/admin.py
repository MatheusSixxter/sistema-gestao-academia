from django.contrib import admin
from equipmentsentry.models import EquipmentEntry


class EquipmentEntryAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'supplier', 'quantity', 'total_value', 'purchase_date',]
    

admin.site.register(EquipmentEntry, EquipmentEntryAdmin)
