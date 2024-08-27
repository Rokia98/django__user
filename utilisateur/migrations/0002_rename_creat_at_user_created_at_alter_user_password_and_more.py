# Generated by Django 5.1 on 2024-08-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='creat_at',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='pseudo',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
