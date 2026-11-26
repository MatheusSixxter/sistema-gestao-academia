from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from suppliers.models import Supplier
from suppliers.forms import SupplierForm
from suppliers.serializer import SupplierSerializer
from django.urls import reverse_lazy


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 6
    permission_required = 'suppliers.view_supplier'

    def get_queryset(self):
        queryset = Supplier.objects.all()

        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset



   

class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    permission_required = 'suppliers.view_supplier'
   



class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    template_name = 'supplier_create.html'
    form_class = SupplierForm
    success_url = reverse_lazy('suppliers_list')
    permission_required = 'suppliers.add_supplier'




class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Supplier
    template_name = 'supplier_update.html'
    form_class = SupplierForm
    permission_required = 'suppliers.change_supplier'


    def get_success_url(self):
        return reverse_lazy('suppliers_detail', kwargs={'pk': self.object.pk})
     


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('suppliers_list')
    permission_required = 'suppliers.delete_supplier'
   


#-----------------------------------------------------------------------------------------------------------------------     
#VIEWS DA API DE SUPPLIER:

class SupplierListCreateAPIView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
        
              
              
              
            


