# Generated by Django 4.0.9 on 2023-02-06 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratos',
            name='taxa',
            field=models.CharField(max_length=25, verbose_name='Taxa Escritório'),
        ),
        migrations.AlterField(
            model_name='contratos',
            name='valor',
            field=models.CharField(max_length=25),
        ),
    ]