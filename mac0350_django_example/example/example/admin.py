from django.contrib import admin
from .models import Usuario, Perfil, Servico, Exame, Pessoa

class UsuarioInline(admin.StackedInline):
    model = Usuario
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    inlines = (UsuarioInline,)

admin.site.register(Perfil)
# admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Servico)
admin.site.register(Exame)
admin.site.register(Usuario)#, UsuarioAdmin)
# admin.site.register(Realizou)
#admin.site.register(Usuario_Possui_Perfil)
