
from .views import modifierEleve, index
from .views import ajouter
from django.urls import path


urlpatterns=[
    path('', ajouter),
    path( 'ajouter', modifierEleve), 
    path( 'index' , index)
]