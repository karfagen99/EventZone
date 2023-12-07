import django_filters
from django.forms import SelectMultiple

from .models import agency, category, services, solutionPlans, contractor
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
    price = django_filters.OrderingFilter(choices=PRICE_CHOICES, label='Цена')
    category__categorieslist = django_filters.ChoiceFilter(choices=CATEGORY_CHOICES, label='Категория')
    title = django_filters.CharFilter(lookup_expr='contains',label='Поиск по названию')
    class Meta:
         model = agency
         fields = ['price','category__categorieslist','title']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(agencyFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['price'].field.widget.attrs.update({'class': 'budget__input'})
        self.filters['category__categorieslist'].field.widget.attrs.update({'class': 'budget__input'})
        self.filters['title'].field.widget.attrs.update({'class': 'budget__input'})



class planFilter(django_filters.FilterSet):

    class Meta:
        model = solutionPlans
        fields = ['plan']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(planFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['plan'].field.widget.attrs.update({'class': 'text-field__input'})


class contractorFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='contains',label='Поиск по названию')

    class Meta:
         model = contractor
         fields = ['title']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(contractorFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['title'].field.widget.attrs.update({'class': 'budget__input'})

