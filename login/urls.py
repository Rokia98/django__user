from .views import login
from django.urls import path

app_name='login'

urlpatterns=[
    path('', login ,name ='login'),
]