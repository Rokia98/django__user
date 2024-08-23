from .views import rapport
from django.urls import path

app_name= 'rapport'

urlpatterns=[
    path( '', rapport, name= 'rapport'),
]