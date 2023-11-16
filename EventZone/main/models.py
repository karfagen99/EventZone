from django.db import models

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

class pricelist(models.Model):
    agent = models.ForeignKey(agency, on_delete=models.CASCADE, verbose_name='агентство')
    price = models.CharField(max_length=6, verbose_name='Стоимость услуги')
    description = models.CharField(max_length=200, verbose_name='Описание')
    def __str__(self):
        return self.description

class gallery(models.Model):
    agent = models.ForeignKey(agency, on_delete=models.CASCADE, verbose_name='агентство')
    description = models.CharField(max_length=200, verbose_name='Описание')
    photo = models.ImageField(upload_to='images/', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.description


