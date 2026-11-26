from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def RegisterView(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')

    else:
        user_form = UserCreationForm()

    return render(request,
                  'register.html', 
                  {'user_form': user_form})




def LoginView(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect ('dashboards')

    else:
        login_form = AuthenticationForm()


    return render(request,
                   'login.html',
                   {'login_form': login_form})
       



@login_required
@require_POST
def LogoutView(request):
    logout(request)
    return redirect('login')