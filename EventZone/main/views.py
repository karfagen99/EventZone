from django.shortcuts import render, get_object_or_404
"""
from .models import Auto
"""
from django.views.generic.list import ListView
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def agency(request):
    return render(request, 'main/agency.html')