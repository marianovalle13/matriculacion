from django.contrib import admin
from .models import *
# Register your models here.

#Modelos ya registradas
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Nota)
admin.site.register(MatriculacionAlumno)
admin.site.register(MatriculacionProfesor)