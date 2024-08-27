from django.db import models

# Définir les choix correctement pour les classes
CHOICES_MATIERE = (
    ('Mathematique', 'Mathematique'),
    ('PC', 'PC'),
    ('EPS', 'EPS'),
    ('Anglais', 'Anglais'),
    ('SVT', 'SVT'),
    ('Philosophie', 'Philosophie'),
    ('Francais', 'Francais'),
)

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
)

# Modèle correspondant au formulaire
class Teacher(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    matricule = models.CharField(max_length=250)
    date = models.DateField()
    matiere = models.CharField(max_length=20, choices=CHOICES_MATIERE, verbose_name="Matiere")
    telephone = models.CharField(max_length=15)
    city = models.CharField(max_length=250)
