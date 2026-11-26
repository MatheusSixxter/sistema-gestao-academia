from django.contrib import admin
from exercises.models import Exercise


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','muscle_group', 'equipament', 'description', 'active',]
    search_fields = ['name',]

admin.site.register(Exercise, ExerciseAdmin)
