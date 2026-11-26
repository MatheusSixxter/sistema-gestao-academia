from django.urls import path
from . import views


urlpatterns = [
    path('athletes/list/', views.AthleteListView.as_view() , name='athletes_list'),

    path('athletes/create/', views.AthleteCreateView.as_view(), name='athletes_create'),

    path('athletes/<int:pk>/detail/', views.AthleteDetailView.as_view(), name='athletes_detail'),

    path('athletes/<int:pk>/update/', views.AthleteUpdateView.as_view(), name='athletes_update'),

    path('athletes/<int:pk>/delete/', views.AthleteDeleteView.as_view(), name='athletes_delete'),


    #URLS DA API DE ATHLETE:
    
    path('api/v1/athletes/', views.AthleteListCreateAPIView.as_view(), name='athlete-list-create-api-view'),

    path('api/v1/athletes/<int:pk>/', views.AthleteRetrieveUpdateDestroyAPIView.as_view(), name='athlete-retrieve-update-destroy-api-view'),
        


]