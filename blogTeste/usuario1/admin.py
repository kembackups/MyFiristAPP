from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site
from .models import Nome, Telefone, Endereco, Email



# nome
class NomeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Nome, NomeAdmin)


# Telefone
class TelefoneAdmin(admin.ModelAdmin):
    pass
admin.site.register(Telefone, TelefoneAdmin)

# Endereço

class EnderecoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Endereco, EnderecoAdmin)

# Email

class EmailAdmin(admin.ModelAdmin):
    pass
admin.site.register(Email, EmailAdmin)