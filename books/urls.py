from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    path('toggle/<int:id>/', views.toggle_issue, name='toggle_issue'),
    path('issue/<int:id>/', views.issue_book, name='issue_book'),
    path('student/login/', views.student_login, name='student_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/logout/', views.student_logout, name='student_logout'),

]

