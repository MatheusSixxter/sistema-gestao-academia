from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework import generics
from athletes.models import Athlete
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from athletes.forms import AthleteForm
from athletes.serializer import AthleteSerializer
from dashboards import metrics
from django.urls import reverse_lazy
from django.db.models import Q


class AthleteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Athlete
    template_name = 'athlete_list.html'
    context_object_name = 'athletes'
    paginate_by = 6
    permission_required = 'athletes.view_athlete'


    def get_queryset(self):
        queryset = Athlete.objects.all()

        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(cpf__icontains=search) |
                Q(phone__icontains=search) 

            )
        return queryset



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['athletes_metrics'] = metrics.athletes_metrics()

        return context


    




class AthleteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Athlete
    template_name = 'athlete_create.html'
    form_class = AthleteForm
    success_url = reverse_lazy('athletes_list')
    permission_required = 'athletes.add_athlete'





class AthleteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Athlete
    template_name = 'athlete_detail.html'
    permission_required = 'athletes.view_athlete'




class AthleteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athlete_update.html'
    permission_required = 'athletes.change_athlete'

    def get_success_url(self):
        return reverse_lazy('athletes_detail', kwargs={'pk': self.object.pk})




class AthleteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Athlete
    template_name = 'athlete_delete.html'
    success_url = reverse_lazy('athletes_list')
    permission_required = 'athletes.delete_athlete'



#------------------------------------------------------------------------------------------------------------------------
#VIEWS DA API DE ATHLETE:

class AthleteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer



class AthleteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer