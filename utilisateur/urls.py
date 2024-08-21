from .views import index, modifierUtilisateur
from django.urls import path

urlpatterns={
       path ('', index, name='index'),
     path('modifierUtilisateur/', modifierUtilisateur),
}

