from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('q1/',views.q1,name='q1'),
    path('q2/',views.q2,name='q2'),
    path('h1/',views.h1,name='h1'),
]