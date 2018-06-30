from django.db import models

# Create your models here.

#Clase Persona donde muchas otras heredaran de ella
class Persona(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	nombre = models.CharField("Nombre",max_lenght=30)
	apellido = models.CharField("Apellido", max_lenght=30)
	email = models.EmailField("Email", max_length=100)
	telefono = models.CharField("Telefono", max_length=90)
	dni = models.PositiveIntegerField("D.N.I")


#Clase Alumno hereda atributos de Persona
class Alumno (Persona):
	pass

	class Meta:
		verbose_name="Alumno"
		verbose_name_plural="Alumnos";



#Clase Profesor herda atributos de Persona
class Profesor (Persona):
	pass

	class Meta:
		verbose_name="Profesor"
		verbose_name_plural="Profesor"
		

