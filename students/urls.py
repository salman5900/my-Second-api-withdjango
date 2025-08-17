from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student_web, name='student_web'),
]