# Generated by Django 4.0.9 on 2023-02-05 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_alter_sede_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sede',
            name='cnpj',
            field=models.CharField(max_length=15, verbose_name='CNPJ'),
        ),
    ]