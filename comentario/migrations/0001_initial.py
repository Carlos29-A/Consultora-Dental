# Generated by Django 5.1.3 on 2024-12-10 07:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('citas', '0003_alter_citas_id_usuario'),
        ('dentista', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=100)),
                ('calificacion', models.IntegerField()),
                ('fecha_creacion', models.DateField()),
                ('cita_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.citas')),
                ('dentista_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dentista.dentista')),
                ('paciente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comentario',
                'verbose_name_plural': 'comentarios',
            },
        ),
    ]