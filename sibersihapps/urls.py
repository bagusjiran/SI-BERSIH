from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='index'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('registerpage/', views.registerpage, name='registerpage'),
]