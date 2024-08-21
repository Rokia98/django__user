from .views import ajouterprofesseur,index
from.views import modifierProfesseur
from django.urls import path

urlpatterns = {

    path('', index, name ='index'),
    path('modifierProfesseur/', modifierProfesseur),
     path ('ajouterProfesseur/', ajouterprofesseur),
}



