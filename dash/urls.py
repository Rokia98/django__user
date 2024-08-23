from django.urls import path
from .views import dashbord

app_name= 'dash'
urlpatterns=[
    path('',dashbord ,name = 'dash'),
]