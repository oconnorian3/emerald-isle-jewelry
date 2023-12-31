from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('', views.render_contact_form, name='contact'),
    path('success/', views.contact_success, name='contact_success'),
]
