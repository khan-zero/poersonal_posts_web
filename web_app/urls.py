from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='index'),
    path('register/sign-in-up/', views.log_in, name='login'),
    path('archive/', views.archive, name='archive'),
    path('contact/', views.contact, name='archive')
]
