from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import FAQ

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

