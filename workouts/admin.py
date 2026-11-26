from django.contrib import admin
from workouts.models import WorkoutPlan, WorkoutExercise


class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'athlete')
    search_fields = ('name', 'athlete__name')

    inlines = [WorkoutExerciseInline]