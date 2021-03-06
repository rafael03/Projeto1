from usuarios.models import NovoUsuario
from django.contrib import admin

class AdministradorUsuario(admin.TabularInline):
    model = NovoUsuario
    extra = 3

class NovoUsuarioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['Usuario_nome']}),
        ('Date Information',    {'fields': ['Hora_cadastro'], 'classes': ['collapse']}),
    ]
    inlines= [AdministradorUsuario]
    list_display = ('Usuario_nome', 'Hora_cadastro')



admin.site.register(NovoUsuario, NovoUsuarioAdmin)
