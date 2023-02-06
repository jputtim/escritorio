from django.contrib import admin

from core.forms import ClientesFormAdmin

from .models import Clientes

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    form = ClientesFormAdmin

    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('cpf', 'nome_completo', 'data_de_nascimento', 'sexo', 'estado_civil', 'nacionalidade', 'naturalidade','rg', 'orgao', 'ocupacao')
        }),
        ('Filiação', {
            'fields': ('mae', 'pai')
        }),
        ('Contato', {
            'fields': ('telefone', 'email')
        }),
        ('Contato Secundário', {
            'fields': ('tipo_contato','telefone_contato','nome_contato')
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

admin.site.register(Clientes, ClientesAdmin)