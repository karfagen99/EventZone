# Generated by Django 4.2.7 on 2023-12-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_book_solution_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_solution',
            name='book_date',
            field=models.DateField(default='', verbose_name='Дата'),
        ),
    ]
