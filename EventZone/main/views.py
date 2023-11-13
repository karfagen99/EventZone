from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic.list import ListView
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def agencies(request):
    Agency = agency.objects.all()
    return render(request, 'main/agency.html',{'Agency': Agency})

def agencieslayout(request,pk):
    Agency = get_object_or_404(agency, pk= pk)
    return render(request, 'main/agencylayout.html', {'Agency': Agency})

def registration(request):
    return render(request, 'main/registration.html')

def profile(request):
    return render(request, 'main/profile.html')

def contacts(request):
    return render(request, 'main/contacts.html')

