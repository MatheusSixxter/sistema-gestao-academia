from django.db import models
from athletes.models import Athlete
from exercises.models import Exercise


class WorkoutPlan(models.Model):
    athlete = models.ForeignKey(
        Athlete,
        on_delete=models.PROTECT,
        related_name='workout_plans'
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    status = models.CharField(
        max_length=10,
        choices=[
            ('active', 'Ativo'),
            ('inactive', 'Inativo'),
        ],
        default='active'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.name} - {self.athlete.name}"






class WorkoutExercise(models.Model):
    workout_plan = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.CASCADE,
        related_name='exercises'
    )

    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.PROTECT,
        related_name='workout_plans'
    )

    order = models.PositiveSmallIntegerField(default=1)
    sets = models.PositiveSmallIntegerField(default=3)
    repetitions = models.CharField(max_length=30, default='12')

    weight_kg = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    rest_seconds = models.PositiveSmallIntegerField(default=60)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(
                fields=['workout_plan', 'order'],
                name='unique_exercise_order_per_plan'
            )
        ]

    def __str__(self):
        return f"{self.workout_plan.name} - {self.exercise}"