
from .views import edit, list, update, delete
from django.urls import path

app_name = 'Eleve'

urlpatterns=[
    path('', edit, name ='edit'),
    path('update/<str:pk>/', update, name="update"),
    path( 'list' , list , name=  'list'),
    path('delete/<int:pk>/', delete, name='delete'),


]