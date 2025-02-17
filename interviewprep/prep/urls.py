# prep/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_technology, name='interview_preparation'),
    path('start/', views.interview_preparation, name='start'),
    path('contact/', views.select_contactform, name='contact'),
    

]
