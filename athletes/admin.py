from django.contrib import admin
from athletes.models import Athlete


class AthleteAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'phone', 'plan', 'status',]
    search_fields = ['name',]

admin.site.register(Athlete, AthleteAdmin)