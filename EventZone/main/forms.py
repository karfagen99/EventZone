from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.fields import DateField

from .models import FAQ, book_solution, place, plans


class FeedbackForm(ModelForm):
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'text-field faq', 'placeholder': 'Имя'}),
    )
    email = forms.CharField(
        label='Почта',
        widget=forms.TextInput(attrs={'class': 'text-field faq', 'placeholder': 'Почта'}),
    )
    question = forms.CharField(
        label='Вопрос',
        widget=forms.TextInput(attrs={'class': 'feedback faq', 'placeholder': ''}),
    )
    class Meta:
        model = FAQ
        fields = ['name','email','question']

class BookingForm(ModelForm):
    PLAN_CHOICES = (
        ('0','Эконом'),
        ('1', 'Стандарт'),
        ('2', 'Премиум'),
    )
    plan = forms.ModelChoiceField(
        queryset=plans.objects.all(),
        label='Тариф',
        widget=forms.Select(attrs={'class': 'text-field__input'})
    )
    book_date = forms.CharField(
        label='Дата',
        widget=forms.TextInput(attrs={'type':'date','class': 'text-field__input'})
    )
    book_place = forms.ModelChoiceField(
        queryset=place.objects.all(),
        label='Площадка',
        widget=forms.Select(attrs={'class': 'text-field__input'})
    )
    class Meta:
        model = book_solution
        fields = ['plan','book_date','book_place']

