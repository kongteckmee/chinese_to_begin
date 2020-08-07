from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_courses, name='store'),
    path('<store_id>', views.course_detail, name='course_detail'),
]
