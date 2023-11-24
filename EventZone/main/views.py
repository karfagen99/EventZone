from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import SignUpForm, LoginForm, FeedbackForm
from .models import *
from django.views.generic.list import ListView
from django.views.generic import DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .filters import agencyFilter



def index(request):
    return render(request, 'main/index.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def agencyFilt(request):
    f = agencyFilter(request.GET, queryset=agency.objects.all())
    return render(request,'main/agency.html',{'filter': f})


def agencieslayout(request,pk):
    Agency = get_object_or_404(agency, pk= pk)
    Gallery = gallery.objects.all().filter(agent=Agency)
    Pricelist = pricelist.objects.all().filter(agent=Agency)
    return render(request, 'main/agencylayout.html', {'Agency': Agency,'Gallery': Gallery,'Pricelist': Pricelist})

def registration(request):
    return render(request, 'main/registration.html')

def profile(request):
    return render(request, 'main/profile.html')

def contacts(request):
    error=''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/')
        else:
            error = 'Не верные данные'

    form = FeedbackForm()

    data ={'form':form}

    return render(request, 'main/contacts.html', data)

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})

def login_page(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile")
            else:
                return redirect("/")


    return render(request, "login_page.html", {"form": form})

def reservation(request):
    return render(request, 'main/reservation.html')