# Generated by Django 5.1 on 2024-08-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=10)),
                ('matricule', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('classe', models.CharField(choices=[('Terminale', 'Terminale'), ('Premiere', 'Première'), ('Seconde', 'Seconde'), ('Troisieme', 'Troisième'), ('Quatrieme', 'Quatrième'), ('Cinqieme', 'Cinquième'), ('Sixieme', 'Sixième')], max_length=20, verbose_name='classe')),
                ('telephone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=250)),
            ],
        ),
    ]
