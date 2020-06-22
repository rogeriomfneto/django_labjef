from django.contrib import admin
from .models import Usuario, Perfil, Servico, Realizou

# class PerfilInline(admin.TabularInline):
#     model = Usuario_Possui_Perfil
#     extra = 1

# class UsuarioAdmin(admin.ModelAdmin):
#     inlines = (PerfilInline,)

admin.site.register(Perfil)
admin.site.register(Usuario)#, UsuarioAdmin)
admin.site.register(Servico)
admin.site.register(Realizou)
#admin.site.register(Usuario_Possui_Perfil)
