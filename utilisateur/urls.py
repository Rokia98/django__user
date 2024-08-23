from .views import index, modifierUtilisateur
from django.urls import path

app_name= 'utilisateur'
urlpatterns=[
     path ('', index, name='index'),
     path('modifierUtilisateur/', modifierUtilisateur,name= 'modifierUtilisateur'),
]

