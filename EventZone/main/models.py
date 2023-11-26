from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class agency(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название агентства')
    short_description = models.CharField(max_length=200, verbose_name='Короткое описание')
    description = models.CharField(max_length=600, verbose_name='Описание')
    price = models.CharField(max_length=5, verbose_name='Цена')
    people = models.CharField(max_length=4, verbose_name='Количество человек')
    picture = models.ImageField(upload_to='images/', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Агентство'
        verbose_name_plural = 'Агентства'

class solutions(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название решения')
    description = models.CharField(max_length=600, verbose_name='Описание')
    picture = models.ImageField(upload_to='images/', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'

class plans(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название тарифа')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

class services(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название услги')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class solutionPlans(models.Model):
    solution = models.ForeignKey(solutions, on_delete=models.CASCADE, verbose_name='Решение')
    plan = models.ForeignKey(plans, on_delete=models.CASCADE, verbose_name='Тариф')
    service = models.ForeignKey(services, on_delete=models.CASCADE, verbose_name='Услуга')

    def __str__(self):
        return str(self.solution) + ' ' + str(self.plan) + ' ' + str(self.service)
    class Meta:
        verbose_name = 'Услуга в тарифе'
        verbose_name_plural = 'Услуги в тарифах'

class pricelist(models.Model):
    agent = models.ForeignKey(agency, on_delete=models.CASCADE, verbose_name='агентство')
    price = models.CharField(max_length=6, verbose_name='Стоимость услуги')
    description = models.CharField(max_length=200, verbose_name='Описание')
    def __str__(self):
        return self.description
    class Meta:
        verbose_name = 'Прайс лист'
        verbose_name_plural = 'Прайс листы'

class gallery(models.Model):
    agent = models.ForeignKey(agency, on_delete=models.CASCADE, verbose_name='Агентство', null=True)
    solution = models.ForeignKey(solutions, on_delete=models.CASCADE, verbose_name='Решение', null=True)
    description = models.CharField(max_length=200, verbose_name='Описание')
    photo = models.ImageField(upload_to='images/', verbose_name='Фото', blank=True, null=True)


    def __str__(self):
        return self.description
    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'

class categorieslist(models.Model):
    title = models.CharField(max_length=30, verbose_name='Категория')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
class category(models.Model):
    agent = models.ForeignKey(agency, on_delete=models.CASCADE, verbose_name='агентство')
    categorieslist = models.ForeignKey(categorieslist, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return str(self.agent)
    class Meta:
        verbose_name = 'Категория агентства'
        verbose_name_plural = 'Категории агентств'
class FAQ(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    email = models.CharField(max_length=40, verbose_name='Почта')
    question = models.CharField(max_length=30, verbose_name='Вопрос')

    def __str__(self):
        return self.question
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'