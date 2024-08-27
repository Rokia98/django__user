from django.db import models

# Définir les choix correctement pour les classes
CHOICES_CLASSE = (
   ('Terminale', 'Terminale'),
    ('Premiere', 'Première'),
    ('Seconde', 'Seconde'),
    ('Troisieme', 'Troisième'),
    ('Quatrieme', 'Quatrième'),
    ('Cinqieme', 'Cinquième'),
    ('Sixieme', 'Sixième'),
)


GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
)

# Modèle correspondant au formulaire
class Student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    matricule = models.CharField(max_length=250)
    date = models.DateField()
    classe = models.CharField(max_length=20, choices=CHOICES_CLASSE, verbose_name="classe")
    telephone = models.CharField(max_length=15)
    city = models.CharField(max_length=250)
