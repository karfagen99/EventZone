from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('agencies/<int:pk>', views.agencieslayout, name ='agency_detail'),
    path('profile', views.profile, name='profile'),
    path('contacts', views.contacts, name='contacts'),
    path('agencies', views.agencyFilt, name='agencies'),
    path('reservation/<int:pk>', views.reservation, name='reservation'),
    path('ticket', views.ticket, name='ticket'),
    path('solutions', views.solutionsPage, name='solutions'),

]