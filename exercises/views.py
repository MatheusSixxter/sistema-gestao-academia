from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from exercises.models import Exercise
from exercises.forms import ExerciseForm
from exercises.serializer import ExerciseSerializer
from django.urls import reverse_lazy
from django.db.models import Q



class ExerciseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Exercise
    template_name = 'exercise_list.html'
    context_object_name = 'exercises'
    paginate_by = 6
    permission_required = 'exercises.view_exercise'

    def get_queryset(self):
        queryset = Exercise.objects.all()

        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(equipament__icontains=search)

            )

        return queryset



class ExerciseDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Exercise
    template_name = 'exercise_detail.html'
    permission_required = 'exercises.view_exercise'



class ExerciseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Exercise
    template_name = 'exercise_create.html'
    form_class = ExerciseForm
    success_url = reverse_lazy('exercises_list')
    permission_required = 'exercises.add_exercise'



class ExerciseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Exercise 
    template_name = 'exercise_update.html'
    form_class = ExerciseForm
    permission_required = 'exercises.change_exercise'

    def get_success_url(self):
        return reverse_lazy('exercises_detail', kwargs={'pk': self.object.pk})



class ExerciseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Exercise
    template_name = 'exercise_delete.html'
    success_url = reverse_lazy('exercises_list')
    permission_required = 'exercises.delete_exercise'



    
        
 #----------------------------------------------------------------------------------------------------------------------

#Views da API de exercise:

class ExerciseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer



class ExerciseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
              

        
              
              
              
            


