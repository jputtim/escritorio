# Generated by Django 4.0.9 on 2023-02-03 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=255)),
                ('nome_fantasia', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=15, verbose_name='CNPJ')),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('cep', models.CharField(blank=True, max_length=10, verbose_name='CEP')),
                ('cidade', models.CharField(blank=True, max_length=255)),
                ('uf', models.CharField(blank=True, max_length=25, verbose_name='Estado')),
                ('bairro', models.CharField(blank=True, max_length=255)),
                ('logradouro', models.CharField(blank=True, max_length=255)),
                ('numero_residencia', models.CharField(blank=True, max_length=10, verbose_name='Número')),
                ('complemento_endereco', models.CharField(blank=True, max_length=255, verbose_name='Complemento')),
                ('logo', models.ImageField(upload_to='uploads/logo/')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sede',
            },
        ),
    ]