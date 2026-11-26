from athletes.models import Athlete
from equipments.models import Equipment, CATEGORY_CHOICES
from exercises.models import Exercise
from workouts.models import WorkoutPlan
from suppliers.models import Supplier
from django.db.models import Sum
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.utils import timezone


#Cálculo de media de novos alunos para colocar embaixo.
def average_new_athletes():
    today = timezone.localdate()

    # Primeiro dia do mês atual
    current_month = today.replace(day=1)

    # Primeiro dia dos últimos 6 meses completos
    month_index = current_month.year * 12 + current_month.month - 1 - 6
    start_date = current_month.replace(
        year=month_index // 12,
        month=month_index % 12 + 1
    )

    registrations = (
        Athlete.objects
        .filter(
            enrollment__gte=start_date,
            enrollment__lt=current_month
        )
        .annotate(month=TruncMonth('enrollment'))
        .values('month')
        .annotate(total=Count('id'))
    )

    # Inclui meses sem cadastros na média
    total_registrations = sum(
        item['total'] for item in registrations
    )

    return round(total_registrations / 6, 1)



    
#Métricas de alunos:
def athletes_metrics():
    total_athletes = Athlete.objects.count()
    active_athletes = Athlete.objects.filter(status='active').count()
    inactive_athletes = Athlete.objects.filter(status='inactive').count()
    average_new = average_new_athletes()



    return dict(
        total_athletes = total_athletes,
        active_athletes = active_athletes,
        inactive_athletes = inactive_athletes,
        average_new_athletes = average_new,



    )


#------------------------------------------------------------------------------------------------------------------------
    
#Métricas do Sistema:
def gym_metrics():
   total_workouts = WorkoutPlan.objects.count()
   total_suppliers = Supplier.objects.count()
   total_exercises = Exercise.objects.count()
   total_equipments = Equipment.objects.aggregate(total_sum=Sum('quantity'))['total_sum'] or 0


   return dict(
       total_workouts = total_workouts,
       total_suppliers = total_suppliers,
       total_exercises = total_exercises,
       total_equipments = total_equipments,
       

       
   )



#------------------------------------------------------------------------------------------------------------------------

#GRÁFICOS DO SISTEMA:


# Dados para o gráfico de atletas
def athletes_chart_data():
    athletes = (
        Athlete.objects
        .annotate(month=TruncMonth('enrollment'))
        .values('month')
        .annotate(total=Count('id'))
        .order_by('month')
    )

    return {
        'months': [
            item['month'].strftime('%m/%Y')
            for item in athletes
        ],
        'values': [
            item['total']
            for item in athletes
        ]
    }


# Dados para o gráfico de equipamentos
def equipments_chart_data():
    equipments = (
        Equipment.objects
        .values('category')
        .annotate(total=Count('quantity'))
    )

    equipment_data = {
        item['category']: item['total']
        for item in equipments
    }

    return {
        'categories': [
            label for value, label in CATEGORY_CHOICES
        ],
        'values': [
            equipment_data.get(value, 0)
            for value, label in CATEGORY_CHOICES
        ]
    }