from django.urls import path
from . import views

urlpatterns = [
    path('<store_id>', views.checkout, name='checkout')
]
