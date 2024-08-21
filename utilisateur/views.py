from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, "utilisateur/index.html")

def modifierUtilisateur(request):
    return render (request, "utilisateur/modifierUtilisateur.html")

