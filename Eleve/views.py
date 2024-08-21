from django.shortcuts import render
# l'ensembles de fonction 
# Create your views here.

def ajouter(request):
    return render (request,"Eleve/ajouter.html")

def modifierEleve(request):
    return render (request,"Eleve/modifierEleve.html")

def index(request):
    return render (request,"Eleve/index.html")






