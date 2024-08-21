from django.shortcuts import render

# Create your views here.
def modifierProfesseur(request):
    return render (request,"professeur/modifierProfesseur.html")

def ajouterprofesseur(request):
    return render (request,"professeur/professeur.html")

def index(request):
    return render (request,"professeur/index.html")

