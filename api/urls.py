
from . import views
from django.urls import path

urlpatterns = [
    path('register/',views.patient_register),
    path('login/',views.patient_login),
]