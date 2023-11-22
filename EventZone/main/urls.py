from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('agencies', views.agencies, name='agencies'),
    path('agencies/<int:pk>', views.agencieslayout, name ='agency_detail'),
    path('registration', views.registration, name='registration'),
    path('profile', views.profile, name='profile'),
    path('contacts', views.contacts, name='contacts'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_page, name='login'),
    path('agencies', views.agencyFilt, name='agencies'),

]