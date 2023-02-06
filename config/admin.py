from django.contrib import admin
from config.forms import SedeFormAdmin, AdvogadosFormAdmin
from .models import Sede, Advogados


# Register your models here.
class SedeAdmin(admin.ModelAdmin):
    form = SedeFormAdmin

    fieldsets = (
        ('Empresa', {
            'fields': ('cnpj', 'razao_social', 'nome_fantasia')
        }),
        ('Contato', {
            'fields': ('telefone', 'email')
        }),
        ('Endereço', {
            'fields': ('cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'uf')
        }),
        ('Logomarca', {
            'fields': ('logo',)
        }),

    )

    class Media:
        js=("jquery.mask.min.js","functions.js",)

    readonly_fields = ("criado_por", "criado_em", "atualizado_em")

    # SALVAR USUÁRIO
    def save_model(self, request, obj, form, change):
        if obj.id == None:
            obj.criado_por = request.user
            super().save_model(request, obj, form, change)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(Sede, SedeAdmin)

class AdvogadosAdmin(admin.ModelAdmin):
    form = AdvogadosFormAdmin

    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('cpf', 'nome_completo', 'data_de_nascimento', 'sexo', 'estado_civil', 'nacionalidade')
        }),
        ('Registro Profissional', {
            'fields': ('oab', 'uf_oab')
        }),
        ('Contato', {
            'fields': ('telefone', 'email')
        }),
        ('Endereço', {
            'fields': ('cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'uf', 'complemento_endereco')
        }),
    )

    class Media:
        js=("jquery.mask.min.js","functions.js",)

    readonly_fields = ("criado_por", "criado_em", "atualizado_em")

    # SALVAR USUÁRIO
    def save_model(self, request, obj, form, change):
        if obj.id == None:
            obj.criado_por = request.user
            super().save_model(request, obj, form, change)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(Advogados, AdvogadosAdmin)