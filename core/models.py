from django.db import models
from django.contrib.auth.models import User
from config.models import *

from cpf_field.models import CPFField
from django.utils.html import format_html

# Create your models here.
class Clientes(models.Model):
    nome_completo = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    cpf = CPFField('CPF', unique=True)
    rg = models.CharField('RG',max_length=11)
    orgao =  models.CharField('Expedido por',max_length=150)
    CHOICES_SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField(max_length=1, choices=CHOICES_SEXO)
    CHOICES_ESTADO_CIVIL = (
        ('C', 'Casado'),
        ('D', 'Divorciado'),
        ('S', 'Solteiro'),
    )
    estado_civil = models.CharField(max_length=1, choices=CHOICES_ESTADO_CIVIL)
    naturalidade = models.CharField('Naturalidade', max_length=255, blank=True)
    nacionalidade = models.CharField('Nacionalidade', max_length=255, blank=True)
    ocupacao = models.CharField('Ocupação', max_length=255,  blank=True)
    mae = models.CharField('Mãe', max_length=255,  blank=True)
    pai = models.CharField('Pai', max_length=255,  blank=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, blank=True)
    CHOICES_TIPO = (
        ('C', 'Cônjuge'),
        ('V', 'Vizinho'),
        ('M', 'Mãe'),
        ('P', 'Pai'),
        ('O', 'Outro'),
    )
    tipo_contato = models.CharField(max_length=1, choices=CHOICES_TIPO)
    telefone_contato = models.CharField(max_length=20)
    nome_contato = models.CharField('Nome Contato', max_length=255, blank=True)
    cep = models.CharField('CEP', max_length=10, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    uf = models.CharField('Estado', max_length=25, blank=True)
    bairro = models.CharField(max_length=255, blank=True)
    logradouro = models.CharField(max_length=255, blank=True)
    numero_residencia = models.CharField('Número', max_length=10, blank=True)
    complemento_endereco = models.CharField('Complemento', max_length=255, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)

    def save(self, *args, **kwargs):
        self.nome_completo = self.nome_completo.upper()
        super(Clientes,self).save(*args,**kwargs)
    
    def cpf_format(self):
        num = self.cpf
        return format_html(num[:3]+"."+num[3:6]+"."+num[6:9]+"-"+num[9:])

    def contato(self):
        num = self.telefone
        return format_html("("+num[:2]+") "+num[2:7]+"-"+num[7:])        
    
    def __str__(self):
        return u'%s - %s' % (self.cpf, self.nome_completo)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Contratos(models.Model):
    CHOICES_TIPO = (
        ('N', 'Normal'),
        ('R', 'Risco'),
    )
    CHOICES_TIPO_PGTO = (
        ('V', 'À vista'),
        ('P', 'Parcelado'),
    )
    tipo = models.CharField('Tipo de contrato', max_length=1, choices=CHOICES_TIPO)
    tipo_pagamento = models.CharField('Tipo de pagamento', max_length=1, choices=CHOICES_TIPO_PGTO)
    valor_entrada = models.CharField('Entrada', max_length=25, blank= True)
    parcelas = models.IntegerField(null= True)
    acao = models.CharField('Ação', max_length=255)
    foro_acao = models.CharField('Foro da Ação', max_length=255, default="Teixeira de Freitas - BA")
    foro_execucao = models.CharField('Foro da Execução',max_length=255, default="Teixeira de Freitas - BA")
    valor = models.CharField(max_length=25, blank= True)
    taxa = models.CharField('Taxa Escritório',max_length=25, blank= True)
    honorario = models.DecimalField(max_digits=8, decimal_places=2, default=30, blank= True)
    multa = models.DecimalField(max_digits=8, decimal_places=2, default=20, blank= True)
    mora = models.DecimalField(max_digits=8, decimal_places=2, default=1, blank= True)
    processo = models.CharField(max_length=30, blank=True)
    clientes = models.ManyToManyField(Clientes, blank=True)
    advogados = models.ManyToManyField(Advogados, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)

    def __str__(self):
        return u'%s - %s' % (self.acao, self.clientes)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'