
from .views import modifierEleve, index
from .views import ajouter
from django.urls import path

app_name = 'Eleve'
urlpatterns=[
    path('', ajouter , name= 'ajouter'),
    path( 'ajouter', modifierEleve, name='modifierEleve'), 
    path( 'index' , index , name=  'index')
]