from django.contrib import admin
from config.forms import SedeFormAdmin
from .models import Sede


# Register your models here.
class SedeAdmin(admin.ModelAdmin):
    form = SedeFormAdmin

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