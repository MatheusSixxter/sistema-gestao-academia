from django.urls import path
from . import views


urlpatterns = [
    path('equipments/list/', views.EquipmentListView.as_view() , name='equipments_list'),

    path('equipments/create/', views.EquipmentCreateView.as_view(), name='equipments_create'),

    path('equipments/<int:pk>/detail/', views.EquipmentDetailView.as_view(), name='equipments_detail'),

    path('equipments/<int:pk>/update/', views.EquipmentUpdateView.as_view(), name='equipments_update'),

    path('equipments/<int:pk>/delete/', views.EquipmentDeleteView.as_view(), name='equipments_delete'),


    #URLS DA API DE EQUIPMENT:

    path('api/v1/equipments/', views.EquipmentListCreateAPIView.as_view(), name='equipment-list-create-api-view'),

        
    path('api/v1/equipments/<int:pk>/', views.EquipmentRetrieveUpdateDestroyAPIView.as_view(), name='equipment-retrieve-update-destroy-api-view'),

]