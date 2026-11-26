from rest_framework import serializers
from workouts.models import WorkoutExercise, WorkoutPlan


class WorkoutPlanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WorkoutPlan
        fields = '__all__'


class WorkoutExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutExercise
        fields = '__all__'