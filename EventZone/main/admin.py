from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(agency)
admin.site.register(pricelist)
admin.site.register(gallery)
admin.site.register(category)
admin.site.register(categorieslist)
admin.site.register(FAQ)
admin.site.register(solutions)
admin.site.register(plans)
admin.site.register(services)
admin.site.register(solutionPlans)
admin.site.register(book_solution)
admin.site.register(place)








