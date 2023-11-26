from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import FeedbackForm
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
def solutionsPage(request):
    f = solutions.objects.all()
    return render(request,'main/solutions.html',{'filter':f})

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



def ticket(request):
    return render(request, 'main/ticket.html')

def reservation(request,pk):

    return render(request, 'main/reservation.html')