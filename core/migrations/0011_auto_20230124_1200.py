# Generated by Django 3.1.2 on 2023-01-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_solicitudreserva_estadoreserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudreserva',
            name='estadoreserva',
            field=models.BooleanField(default=False, verbose_name='ESTADO SOLICITUDES'),
        ),
    ]
