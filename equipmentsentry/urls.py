from django.urls import path
from . import views


urlpatterns = [
    path('equipmentsentry/list/', views.EquipmentEntryListView.as_view() , name='equipmentsentry_list'),

    path('equipmentsentry/create/', views.EquipmentEntryCreateView.as_view(), name='equipmentsentry_create'),

    path('equipmentsentry/<int:pk>/detail/', views.EquipmentEntryDetailView.as_view(), name='equipmentsentry_detail'),




    #URLS DA API DE EQUIPMENTENTRY:
    path('api/v1/equipmentsentry/', views.EquipmentEntryListCreateAPIView.as_view(), name='equipmententry-list-create-api-view'),
     
    path('api/v1/equipmentsentry/<int:pk>/', views.EquipmentEntryRetrieveUpdateDestroyAPIView.as_view(), name='equipmententry-retrieve-update-destroy-api-view'),

]