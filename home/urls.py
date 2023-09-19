from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tasklist', views.tasklist, name='tasklist'),
    path('delete_task/<id>/', views.delete_task, name='delete_task')
]
