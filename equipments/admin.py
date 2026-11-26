from django.contrib import admin
from equipments.models import Equipment


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'category', 'description', 'quantity', 'active', 'condition',]
    search_fields = ['title',]

admin.site.register(Equipment, EquipmentAdmin)
