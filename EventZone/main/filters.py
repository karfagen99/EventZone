import django_filters
from django.forms import SelectMultiple

from .models import agency,category
from django import forms


class agencyFilter(django_filters.FilterSet):

    PRICE_CHOICES = (
        ('price', 'По возрастанию'),
        ('-price', 'По убыванию')
    )
    CATEGORY_CHOICES = (
        ('', 'Все'),
        ('1','Свадьба'),
        ('2', 'Юбилей'),
        ('3', 'День рождения'),
        ('4','Корпоратив'),
        ('5','Тематическое'),
        ('6','Спортивное')
    )
    category__categorieslist = django_filters.ChoiceFilter(choices=CATEGORY_CHOICES, label='Категория')
    price = django_filters.OrderingFilter(choices=PRICE_CHOICES, label='Цена')

    class Meta:
         model = agency
         fields = ['category__categorieslist','price']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(agencyFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['price'].field.widget.attrs.update({'class': 'budget__input'})
        self.filters['category__categorieslist'].field.widget.attrs.update({'class': 'budget__input'})



