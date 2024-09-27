# Generated by Django 4.1.5 on 2023-01-31 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_direccion_articulos_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='fecha_ingreso',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='solicitudreserva',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitudreserva',
            name='fecha_salida',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
