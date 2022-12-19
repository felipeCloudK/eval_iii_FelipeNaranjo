# Generated by Django 4.1 on 2022-12-19 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mundial_api', '0002_remove_jugador_equipo_delete_equipo_delete_jugador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('anio_creacuin', models.DateField()),
                ('campeon', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dorsal', models.CharField(max_length=50)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mundial_api.equipo')),
            ],
        ),
    ]
