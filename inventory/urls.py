from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drug/add/', views.add_drug, name='add_drug'),
    path('stock/add/', views.add_stock, name='add_stock'),
    path('stock/delete/<int:pk>/', views.delete_stock, name='delete_stock'),
    path('stock/edit/<int:pk>/', views.edit_stock, name='edit_stock'),
     path('dispense/', views.dispense_drug, name='dispense_drug'),
]
