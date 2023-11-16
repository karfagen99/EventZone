from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

from main.forms import LoginForm


def login_view(request):

    if request.method == 'GET':
        form_log = LoginForm(request.POST or None)

        data = {
            'form_log' : form_log,
        }
        return data

    if request.method == 'POST':
        if request.POST.get('submit') == 'Войти':
            form_log = LoginForm(request.POST or None)
            if form_log.is_valid():
                username = form_log.cleaned_data["username"]
                password = form_log.cleaned_data["password"]
                user = authenticate(request,username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
            data = {
                'form_log' : form_log,
            }
            return data
        return {}

