from .views import ajouterprofesseur,index
from.views import modifierProfesseur
from django.urls import path

app_name ='professeur'
urlpatterns = [
     path('', index, name ='index'),
    path('modifierProfesseur/', modifierProfesseur, name ='modifierProfesseur'),
     path ('ajouterProfesseur/', ajouterprofesseur, name = 'ajouterProfesseur'),


]

   


