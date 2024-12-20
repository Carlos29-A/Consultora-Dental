# Generated by Django 5.1.3 on 2024-12-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dentista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('especialidad', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('correo_electronico', models.EmailField(max_length=254)),
            ],
        ),
    ]
