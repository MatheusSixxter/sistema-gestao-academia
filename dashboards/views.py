from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from . import metrics

@login_required
def DashboardView(request):

    #Calculo das métricas:
    athletes_metrics = metrics.athletes_metrics()
    gym_metrics = metrics.gym_metrics()


    #Calculo de métricas dos gráficos:
    athletes_chart_data = metrics.athletes_chart_data()
    equipments_chart_data = metrics.equipments_chart_data()



    #Contexto pro template e gráficos.
    context = {
        'athletes_metrics': athletes_metrics,
        'gym_metrics':  gym_metrics,




        #Usei json pro js entender os graficos.
        'athletes_chart_data': json.dumps(athletes_chart_data),
        'equipments_chart_data': json.dumps(equipments_chart_data),


    }


    return render(request,
                   'dashboards.html',
                     context)