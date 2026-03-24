from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstPage, name='first'),
    path('second/', views.secondPage, name='second'),
]