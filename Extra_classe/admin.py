from django.contrib import admin

from .models import *

admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Comentario)
admin.site.register(Profdisciplina)
admin.site.register(Atendimento)


