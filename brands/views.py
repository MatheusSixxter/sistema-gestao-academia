from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from brands.models import Brand
from brands.forms import BrandForm
from brands.serializer import BrandSerializer
from django.urls import reverse_lazy


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 6
    permission_required = 'brands.view_brand'

    def get_queryset(self):
        queryset = Brand.objects.all()

        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset



class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    permission_required = 'brands.view_brand'




class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brands_list')
    permission_required = 'brands.add_brand'



class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    permission_required = 'brands.change_brand'

    def get_success_url(self):
        return reverse_lazy('brands_detail', kwargs={'pk': self.object.pk})

    

class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brands_list')
    permission_required = 'brands.delete_brand'

        
#------------------------------------------------------------------------------------------------------------------------

#VIEWS DA API DE BRAND:


class BrandListCreateAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer



class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
