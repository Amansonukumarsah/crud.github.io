from django.urls import path
from . import views 

urlpatterns = [
    path('skill/',views.skills,name='skills')
]
