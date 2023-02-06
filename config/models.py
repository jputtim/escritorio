from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User
from cnpj_field.models import CNPJField

# Create your models here.
class Sede(models.Model):
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    # cnpj = models.CharField('CNPJ',max_length=15)
    cnpj = CNPJField('CNPJ', unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, blank=True)
    cep = models.CharField('CEP', max_length=10, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    uf = models.CharField('Estado', max_length=25, blank=True)
    bairro = models.CharField(max_length=255, blank=True)
    logradouro = models.CharField(max_length=255, blank=True)
    numero_residencia = models.CharField('Número', max_length=10, blank=True)
    complemento_endereco = models.CharField('Complemento', max_length=255, blank=True)
    logo = models.ImageField(upload_to ='uploads/logo/')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)

    def save(self, *args, **kwargs):
        self.razao_social = self.razao_social.upper()
        self.nome_fantasia = self.nome_fantasia.upper()
        super(Sede,self).save(*args,**kwargs)

    def cnpj_format(self):
        num = self.cnpj
        return format_html(num[:2]+"."+num[2:5]+"."+num[5:8]+"/"+num[8:12]+"-"+num[12:14])

    def __str__(self):
        return u'%s - %s' % (self.cnpj, self.razao_social)

    class Meta:
        verbose_name = 'Sede'