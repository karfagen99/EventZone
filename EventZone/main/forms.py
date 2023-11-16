from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm (UserCreationForm):

    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'text-field__input', 'placeholder': 'Пароль'}),
        help_text='',
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'text-field__input', 'placeholder': 'Подтверждение пароля'}),
        help_text='',
    )
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'text-field__input', 'placeholder': 'Логин'}),
            'first_name': forms.TextInput(
                attrs={'class': 'text-field__input', 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(
                attrs={'class': 'text-field__input', 'placeholder': 'Фамилия'}),
            'email': forms.TextInput(
                attrs={'class': 'text-field__input', 'placeholder': 'E-mail'}),
            'password1': forms.PasswordInput(
                attrs={'class': 'text-field__input', 'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(
                attrs={'class': 'text-field__input', 'placeholder': 'Подтверждение пароля'}),
        }
        help_texts = {
            'username': "",
            'password1': "",
            'password2': ""
        }

class LoginForm(forms.Form): # Форма логина

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'text-field__input', 'placeholder': 'Логин'}),
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'text-field__input', 'placeholder': 'Пароль'}),
    )
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'text-field__input', 'placeholder': 'Логин'})
        }
        help_texts = {
            'username': "",
            'password': "",
        }
