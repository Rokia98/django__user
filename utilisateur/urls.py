from .views import edit , list, update, delete
from django.urls import path

app_name= 'utilisateur'
urlpatterns=[
     path ('', list, name='list'),
     path('edit/', edit,name= 'edit'),
     path('update/<str:pk>/', update, name="update"),
     path('delete/<int:pk>/', delete, name='delete'),

]

