from django.urls import path
from dashboards.views import DashboardView


urlpatterns = [
    path('', DashboardView , name='dashboards'),

]
