from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
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
        model = CustomUser
        fields = ('email','password1','password2')
        widgets = {
            'email': forms.TextInput(
                attrs={'class': 'text-field__input', 'placeholder': 'Логин'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
class CustomAuthenticationForm(AuthenticationForm):

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
        model = CustomUser
        fields = ('username','password')