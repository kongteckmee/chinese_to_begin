from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_courses, name='store'),
    path('<int:store_id>/', views.course_detail, name='course_detail'),
    path('add/', views.add_course, name='add_course'),
    path('edit/<int:store_id>/', views.edit_course, name='edit_course'),
    path('delete/<int:store_id>/', views.delete_course, name='delete_course'),
]
