
from django import forms
from django.forms.widgets import RadioSelect
from .models import Student


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
# class StudentModels(forms.Form):
#     first_name = forms.CharField(max_length=250)
#     last_name = forms.CharField(max_length=250)
#     gender = forms.ChoiceField(choices=GENDER_CHOICES, label= "le genre")
#     matricule = forms.CharField(max_length=250)
#     date = forms.DateField()
#     matiere = forms.ChoiceField(choices=CHOICES_CLASSE, label="classe")
#     telephone = forms.CharField(max_length=15)
#     city = forms.CharField(max_length=250)

class EleveForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "gender", "matricule", "date", "classe", "telephone", "city"]

        widgets = {
            'gender': forms.Select,  # Utilisation de boutons radio pour le choix du genre
            'classe': forms.Select,  # Liste déroulante pour le choix de la classe
            'date': forms.DateInput(attrs={'type': 'date'}),  # Champ de date avec un sélecteur de date
        }
