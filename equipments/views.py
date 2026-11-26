from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from equipments.models import Equipment
from brands.models import Brand
from equipments.forms import EquipmentForm
from equipments.serializer import EquipmentSerializer
from .models import Equipment, CATEGORY_CHOICES, CONDITION_CHOICES
from django.urls import reverse_lazy


class EquipmentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Equipment
    template_name = 'equipment_list.html'
    context_object_name = 'equipments'
    paginate_by = 6
    permission_required = 'equipments.view_equipment'

    def get_queryset(self):
        queryset = Equipment.objects.select_related('brand').all()

        title = self.request.GET.get('title')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        condition = self.request.GET.get('condition')


        if title:
            queryset = queryset.filter(title__icontains=title)


        if category:
            queryset = queryset.filter(category=category)


        if brand:
            queryset = queryset.filter(brand_id=brand)


        if condition:
            queryset = queryset.filter(condition__icontains=condition)


        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['brands'] = Brand.objects.all() #brands é o context name de Brand
        context['categories'] = CATEGORY_CHOICES
        context['conditions'] = CONDITION_CHOICES

        return context





class EquipmentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Equipment
    template_name = 'equipment_detail.html'
    permission_required = 'equipments.view_equipment'




class EquipmentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Equipment
    template_name = 'equipment_create.html'
    form_class = EquipmentForm
    success_url = reverse_lazy('equipments_list')
    permission_required = 'equipments.add_equipment'
    

    


class EquipmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Equipment
    template_name = 'equipment_update.html'
    form_class = EquipmentForm
    permission_required = 'equipments.change_equipment'

    def get_success_url(self):
        return reverse_lazy('equipments_detail', kwargs={'pk': self.object.pk})

    

class EquipmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Equipment
    template_name = 'equipment_delete.html'
    success_url = reverse_lazy('equipments_list')
    permission_required = 'equipments.delete_equipment'



#------------------------------------------------------------------------------------------------------------------------

#VIEWS DA API DE EQUIPMENT:

class EquipmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    