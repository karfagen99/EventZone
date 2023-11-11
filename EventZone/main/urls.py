from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('agencies', views.agencies, name='agencies'),
    path('agencies/<int:pk>', views.agencieslayout, name ='agency_detail')
]