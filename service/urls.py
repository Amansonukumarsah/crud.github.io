from django.urls import path
from . import views 

urlpatterns = [
    path('skills/',views.service,name='service') 
]
