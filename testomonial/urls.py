from django.urls import path
from .views import add_testimonial

urlpatterns = [
    path('add_testimonial/', add_testimonial, name='add_testimonial'),
]