# Generated by Django 3.1.3 on 2020-11-30 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201129_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cortinas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
