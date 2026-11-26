from django.urls import path
from . import views


urlpatterns = [
    path('exercises/list/', views.ExerciseListView.as_view() , name='exercises_list'),

    path('exercises/create/', views.ExerciseCreateView.as_view(), name='exercises_create'),

    path('exercises/<int:pk>/detail/', views.ExerciseDetailView.as_view(), name='exercises_detail'),

    path('exercises/<int:pk>/update/', views.ExerciseUpdateView.as_view(), name='exercises_update'),

    path('exercises/<int:pk>/delete/', views.ExerciseDeleteView.as_view(), name='exercises_delete'),


    #URLS DE EXERCISES:

    path('api/v1/exercises/', views.ExerciseListCreateAPIView.as_view(), name='exercise-list-create-api-view'),
        
    path('api/v1/exercises/<int:pk>/', views.ExerciseRetrieveUpdateDestroyAPIView.as_view(), name='exercise-retrieve-update-destroy-api-view'),

]