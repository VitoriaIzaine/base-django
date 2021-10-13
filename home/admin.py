from django.contrib import admin
from .models import Categoria, Curso

class datCurso(admin.ModelAdmin):
    list_display = ('id','titulo', 'descricao', 'datainicio', 'mostrar' )
    list_editable = ('mostrar',)
    list_display_links = ('titulo',)
    search_fields = ('titulo',)
    list_per_page = 2
    list_filter = ('titulo',)

admin.site.register(Categoria)
admin.site.register(Curso,datCurso)
