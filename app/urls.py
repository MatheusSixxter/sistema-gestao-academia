from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #Página principal do dashboard:
    path('', include('dashboards.urls')),


    #Login, Logout e Register:
    path('', include('accounts.urls')),



    #CRUD do sistema:
    path('', include('athletes.urls')),
    path('', include('workouts.urls')),
    path('', include('exercises.urls')),
    path('', include('brands.urls')),
    path('', include('equipments.urls')),
    path('', include('suppliers.urls')),
    path('', include('equipmentsentry.urls')),



    #Autenticação da API:
    path('api/v1/', include('authentication.urls')),

    



]
