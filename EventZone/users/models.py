from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=100, verbose_name="Имя")
    middlename = models.CharField(max_length=100, verbose_name="Отчество")
    email = models.EmailField(verbose_name='Почтовый адрес', unique=True)
    fullname = models.CharField(max_length=100, verbose_name="ФИО")
    city = models.CharField(max_length=100, verbose_name="Город")
    age = models.CharField(max_length=3, verbose_name="Возраст")
    photo = models.ImageField(upload_to='images/', verbose_name='Фото', blank=True, null=True)
    status = models.BooleanField(default=False, verbose_name='Подтверждение аккаунта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def str(self):
        return self.fullname