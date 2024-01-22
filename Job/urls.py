from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name="index"),
    path('login/',views.Home,name="home"),
    path('register/',views.Register,name="register"),
    path('view/',views.View,name="view"),
    path('job_position/<str:pk>',views.Job_Position,name='job_position'),
    path('company/<str:pk>',views.Company_details,name='company'),
    path('logout/',views.Logout,name='logout'),
    path('companylist/',views.Companylist,name='companylist'),
    path('joblist/',views.Joblist,name='joblist'),
    path('apply_job/<int:job_id>/',views.apply_job, name='apply_job'),
    path('success_page/<int:applied_job_id>/',views.success_page, name='success_page'),
    # path('search/', views.search_results, name='search_results'),
    path('jobcategory/',views.Jobcategory,name='jobcategory'),
] 