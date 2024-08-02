from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.start_task_view, name="rq-test"),
]
