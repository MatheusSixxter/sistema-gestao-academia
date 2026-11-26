from django.views.generic import ListView, CreateView, DetailView
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from equipmentsentry.models import EquipmentEntry
from equipmentsentry.forms import EquipmentEntryForm
from equipmentsentry.serializer import EquipmentEntrySerializer
from django.urls import reverse_lazy
from django.db.models import Q



class EquipmentEntryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = EquipmentEntry
    template_name = 'equipmententry_list.html'
    context_object_name = 'entries'
    paginate_by = 6
    permission_required = 'equipmentsentry.view_equipmententry'

    def get_queryset(self):
        queryset = EquipmentEntry.objects.select_related('equipment', 'supplier')

        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(
                Q(equipment__title__icontains=search) |
                Q(supplier__name__icontains=search)

            )


        return queryset 
    


class EquipmentEntryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = EquipmentEntry
    template_name = 'equipmententry_detail.html'
    permission_required = 'equipmentsentry.view_equipmententry'





class EquipmentEntryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = EquipmentEntry
    template_name = 'equipmententry_create.html'
    form_class = EquipmentEntryForm
    success_url = reverse_lazy('equipmentsentry_list')
    permission_required = 'equipmentsentry.add_equipmententry'




#------------------------------------------------------------------------------------------------------------------------

#VIEWS DA API DE EQUIPMENTENTRY:


class EquipmentEntryListCreateAPIView(generics.ListCreateAPIView):
    queryset = EquipmentEntry.objects.all()
    serializer_class = EquipmentEntrySerializer




class EquipmentEntryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipmentEntry.objects.all()
    serializer_class = EquipmentEntrySerializer





