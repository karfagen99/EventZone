from django.db import models

# Create your models here.
class agency(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название агентства')
    short_description = models.CharField(max_length=200, verbose_name='Короткое описание')
    description = models.CharField(max_length=600, verbose_name='Описание')
    price = models.CharField(max_length=5, verbose_name='Цена')
    people = models.CharField(max_length=4, verbose_name='Количество человек')
    picture = models.ImageField(upload_to='images/', verbose_name='Фото', blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title