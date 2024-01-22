from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home,name="show"),
    path('edit/<str:pk>',views.Edit,name='edit'),
    path('delete/<str:pk>',views.Delete,name='delete'),
]