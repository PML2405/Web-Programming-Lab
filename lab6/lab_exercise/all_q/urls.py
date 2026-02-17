from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('q1/',views.q1,name='q1'),
    path('q2/',views.q2,name='q2'),
    path('q3/',views.q3,name='q3'),
    path('q3_metadata/',views.q3_metadata,name='q3_metadata'),
    path('q3_publisher/',views.q3_publisher,name='q3_publisher'),
    path('q3_reviews/',views.q3_reviews,name='q3_reviews'),
]
