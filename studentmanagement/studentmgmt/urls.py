from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('students/', views.students, name='students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

    path('courses/', views.courses, name='courses'),
    path('courses/delete/<int:id>/', views.delete_course, name='delete_course'),
]
