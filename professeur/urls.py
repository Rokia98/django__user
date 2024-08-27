from .views import update,edit,list, delete
# from.views import modifierProfesseur
from django.urls import path

app_name ='professeur'
urlpatterns = [
     path('', edit, name ='edit'),
     path('update/<str:pk>/', update, name="update"),
     path ('list/', list, name = 'list'),
     path('delete/<int:pk>/', delete, name='delete'),



]

   


