from django.db import models

# Create your models here.

class Eleve(models.Model):
    first_name = models.CharField(max_length=100)  # Prénom de l'élève
    last_name = models.CharField(max_length=100)   # Nom de famille de l'élève
    birth_date = models.DateField()                # Date de naissance
    matricule = models.EmailField()  
    city = models.CharField()  
    niveau = models.CharField()  
    genre=  models.CharField()              
    phone_number = models.CharField(max_length=15) # Numéro de téléphone

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

