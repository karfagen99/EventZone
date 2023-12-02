from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import FeedbackForm, BookingForm
from .models import *
from django.views.generic.list import ListView
from django.views.generic import DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .filters import agencyFilter, planFilter
from django.utils import timezone
from django import forms
from datetime import datetime


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
    book_solutions = book_solution.objects.all().filter(user=request.user)
    return render(request, 'main/profile.html',{'book_solutions': book_solutions})

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



def ticket(request,pk):
    BOOK_solution = get_object_or_404(book_solution, pk=pk)
    BOOK_service = solutionPlans.objects.all().filter(solution=BOOK_solution.solution,plan=BOOK_solution.plan)
    if request.method == 'POST':
        BOOK_solution.delete()
        return redirect('profile')
    return render(request, 'main/ticket.html',{'BOOK_solution': BOOK_solution,'BOOK_service':BOOK_service})

def reservation(request,pk):
    f = solutionPlans.objects.all()
    f1 = plans.objects.all()
    Solution = get_object_or_404(solutions,pk=pk)
    Gallery = gallery.objects.all().filter(solution=Solution)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        userbook = request.user
        booking = form.save(commit=False)
        booking.user = userbook
        booking.solution = Solution
        if form.is_valid():
            today = timezone.now().date()
            checkdate = form.cleaned_data.get('book_date')
            date_format = "%Y-%m-%d"
            checkdate = datetime.strptime(checkdate,date_format).date()
            if checkdate < today:
                raise forms.ValidationError('Выберите дату, начиная с сегодняшнего дня.')
                return
            booking.save()
            return redirect('profile')
        else:
            error = 'Не верные данные'

    form = BookingForm()

    return render(request, 'main/reservation.html', {'filter': f, 'filter1': f1, 'filterPhoto': Gallery,'form': form})