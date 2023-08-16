from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.saved_for_later, name='saved_for_later'),
    path('save_for_later/<int:product_id>/', views.save_for_later, 
         name='save_for_later'),
    path('remove_from_saved/<int:item_id>/', views.remove_from_saved, 
         name='remove_from_saved'),

]
