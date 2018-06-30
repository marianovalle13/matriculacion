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


