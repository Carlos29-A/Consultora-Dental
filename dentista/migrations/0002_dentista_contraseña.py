# Generated by Django 5.1.3 on 2024-12-11 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentista',
            name='contraseña',
            field=models.CharField(default='contraseña_defecto', max_length=30),
        ),
    ]
