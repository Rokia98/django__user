
from django import forms
from django.forms.widgets import RadioSelect
from .models import Teacher


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
class TeacherModel(forms.Form):
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label= "le genre")
    matricule = forms.CharField(max_length=250)
    date = forms.DateField()
    matiere = forms.ChoiceField(choices=CHOICES_MATIERE, label="Matière")
    telephone = forms.CharField(max_length=15)
    city = forms.CharField(max_length=250)

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "gender", "matricule", "date", "matiere", "telephone", "city"]

        widgets = {
            'gender': forms.Select,  # Utilisation de boutons radio pour le choix du genre
            'matiere': forms.Select,  # Liste déroulante pour le choix de la classe
            'date': forms.DateInput(attrs={'type': 'date'}),  # Champ de date avec un sélecteur de date
        }
