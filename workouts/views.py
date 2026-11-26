from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from workouts.models import WorkoutExercise, WorkoutPlan
from workouts.forms import WorkoutPlanForms, WorkoutExerciseForms
from workouts.serializer import WorkoutPlanSerializer, WorkoutExerciseSerializer
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q

#View da ficha de treino:
class WorkoutPlanListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = WorkoutPlan
    template_name = 'workoutplan_list.html'
    context_object_name = 'workouts'
    paginate_by = 6
    permission_required = 'workouts.view_workoutplan'
    


    def get_queryset(self):
        queryset = WorkoutPlan.objects.select_related('athlete')

        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(
                Q(athlete__name__icontains=search) |
                Q(name__icontains=search)

            )

        return queryset




class WorkoutPlanDetailView(LoginRequiredMixin, PermissionRequiredMixin,  DetailView):
     model = WorkoutPlan
     template_name = 'workoutplan_detail.html'
     permission_required = 'workouts.view_workoutplan'



class WorkoutPlanCreateView(LoginRequiredMixin, PermissionRequiredMixin,  CreateView):
    model = WorkoutPlan
    template_name = 'workoutplan_create.html'
    form_class = WorkoutPlanForms
    success_url = reverse_lazy('workoutplans_list')
    permission_required = 'workouts.add_workoutplan'




class  WorkoutPlanUpdateView(LoginRequiredMixin, PermissionRequiredMixin,  UpdateView):
     model = WorkoutPlan
     template_name = 'workoutplan_update.html'
     form_class = WorkoutPlanForms
     permission_required = 'workouts.change_workoutplan'

     def get_success_url(self):
          return reverse_lazy('workoutplans_detail', kwargs={'pk': self.object.pk})



class WorkoutPlanDeleteView(LoginRequiredMixin, PermissionRequiredMixin,  DeleteView):
     model = WorkoutPlan
     template_name = 'workoutplan_delete.html'
     success_url = reverse_lazy('workoutplans_list')
     permission_required = 'workouts.delete_workoutplan'





#View dos exercicios dentro da ficha:

class WorkoutExerciseCreateView(LoginRequiredMixin,  PermissionRequiredMixin, CreateView):
    model = WorkoutExercise
    template_name = 'workoutexercise_create.html'
    form_class =  WorkoutExerciseForms
    permission_required = 'workouts.add_workoutexercise'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workout_plan_id'] = self.workout_plan.pk
        return context


    def dispatch(self, request, *args, **kwargs):
        self.workout_plan = get_object_or_404(
            WorkoutPlan,
            pk=self.kwargs['workout_plan_id']
        )
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        form.instance.workout_plan = self.workout_plan
        return super().form_valid(form)


    def get_success_url(self):
        return reverse(
            'workoutplans_detail',
            kwargs={'pk': self.workout_plan.pk}
        )




class WorkoutExerciseUpdateView(LoginRequiredMixin,  PermissionRequiredMixin, UpdateView):
    model = WorkoutExercise
    template_name = 'workoutexercise_update.html'
    form_class = WorkoutExerciseForms
    permission_required = 'workouts.change_workoutexercise'

    def get_queryset(self):
        return WorkoutExercise.objects.filter(
            workout_plan_id=self.kwargs['workout_plan_id']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workout_plan'] = self.object.workout_plan
        return context

    def get_success_url(self):
        return reverse(
            'workoutplans_detail',
            kwargs={'pk': self.object.workout_plan_id}
        )



class WorkoutExerciseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = WorkoutExercise
    template_name = 'workoutexercise_delete.html'
    permission_required = 'workouts.delete_workoutexercise'

    def get_queryset(self):
        return WorkoutExercise.objects.filter(
            workout_plan_id=self.kwargs['workout_plan_id']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workout_plan'] = self.object.workout_plan
        return context

    def get_success_url(self):
        return reverse(
            'workoutplans_detail',
            kwargs={'pk': self.object.workout_plan_id}
        )



#------------------------------------------------------------------------------------------------------------------------

#VIEWS DA API DE WORKOUT:

#FICHA DE TREINO:
class WorkoutPlanListCreateAPIView(generics.ListCreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class =  WorkoutPlanSerializer


class WorkoutPlanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class =  WorkoutPlanSerializer



# EXERCÍCIOS DENTRO DE UMA FICHA
class WorkoutExerciseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = WorkoutExerciseSerializer

    def get_queryset(self):
        return WorkoutExercise.objects.filter(
            workout_plan_id=self.kwargs['workout_plan_id']
        )

    def perform_create(self, serializer):
        serializer.save(
            workout_plan_id=self.kwargs['workout_plan_id']
        )


class WorkoutExerciseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutExerciseSerializer

    def get_queryset(self):
        return WorkoutExercise.objects.filter(
            workout_plan_id=self.kwargs['workout_plan_id']
        )
