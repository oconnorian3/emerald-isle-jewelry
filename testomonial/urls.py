from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_testimonial, name='add_testimonial'),
    path('testimonial_list/', views.add_testimonial, name='add_testimonial'),
]