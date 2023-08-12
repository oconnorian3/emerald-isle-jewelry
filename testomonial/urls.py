from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_testimonial, name='add_testimonial'),
    path('list/', views.testimonial_list, name='testimonial_list'),
]