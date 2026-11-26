
from django.urls import path
from . import views


urlpatterns = [

    # FICHAS DE TREINO
    path('workoutplan/list/',views.WorkoutPlanListView.as_view(),name='workoutplans_list'),

    path('workoutplan/create/',views.WorkoutPlanCreateView.as_view(),name='workoutplans_create'),

    path('workoutplan/<int:pk>/detail/',views.WorkoutPlanDetailView.as_view(),name='workoutplans_detail'),

    path('workoutplan/<int:pk>/update/', views.WorkoutPlanUpdateView.as_view(),name='workoutplans_update'),

    path('workoutplan/<int:pk>/delete/', views.WorkoutPlanDeleteView.as_view(), name='workoutplans_delete'),


    # EXERCÍCIOS DENTRO DE UMA FICHA
    path('workoutplan/<int:workout_plan_id>/exercises/create/',views.WorkoutExerciseCreateView.as_view(),name='workoutexercises_create'),

    path('workoutplan/<int:workout_plan_id>/exercises/<int:pk>/update/',views.WorkoutExerciseUpdateView.as_view(),name='workoutexercises_update'),

    path('workoutplan/<int:workout_plan_id>/exercises/<int:pk>/delete/',views.WorkoutExerciseDeleteView.as_view(),name='workoutexercises_delete'),






                                             #ROTA DA API DE WORKOUTS:

    # FICHAS DE TREINO
    path('api/v1/workoutplan/', views.WorkoutPlanListCreateAPIView.as_view(), name='workoutplan-list-create-api-view'
    ),

    path('api/v1/workoutplan/<int:pk>/', views.WorkoutPlanRetrieveUpdateDestroyAPIView.as_view(),name='workoutplan-retrieve-update-destroy-api-view'),


     # EXERCÍCIOS DENTRO DA FICHA
    path('api/v1/workoutplan/<int:workout_plan_id>/exercises/', views.WorkoutExerciseListCreateAPIView.as_view(), name='workoutexercise-list-create-api-view'),

    path('api/v1/workoutplan/<int:workout_plan_id>/exercises/<int:pk>/', views.WorkoutExerciseRetrieveUpdateDestroyAPIView.as_view(), name='workoutexercise-retrieve-update-destroy-api-view'),


]