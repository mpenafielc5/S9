# Generated by Django 4.2 on 2024-06-15 05:26

from django.db import migrations, models
import proy_sga.utils


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_asignatura_created_asignatura_update_asignatura_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='cedula',
            field=models.CharField(max_length=10, validators=[proy_sga.utils.valida_cedula]),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='cedula',
            field=models.CharField(max_length=10, validators=[proy_sga.utils.valida_cedula]),
        ),
    ]