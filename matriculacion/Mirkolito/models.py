from django.db import models
from django.conf import settings
# Create your models here.

#Clase Persona donde muchas otras heredaran de ella
class Persona(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	nombre = models.CharField("Nombre",max_length=30)
	apellido = models.CharField("Apellido", max_length=30)
	email = models.EmailField("Email", max_length=100)
	telefono = models.CharField("Telefono", max_length=90)
	dni = models.PositiveIntegerField("D.N.I")
	class Meta:
		verbose_name="Profesor"
		verbose_name_plural="Profesor"
	def __str__(self):
		return "{} {}".format(self.apellido, self.nombre)

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


#Clase Curso
class Curso(models.Model):
	materia = models.CharField("Materia", max_length=30)
	class Meta:
		verbose_name = "Curso"
		verbose_name_plural = "Cursos"
	def __str__(self):
		return "{}".format(self.materia)


#Clase Nota
class Nota(models.Model):
	valor = models.PositiveIntegerField("Nota")
	alumno = models.ForeignKey("Alumno", Alumno)
	curso = models.ForeignKey("Curso", Curso)
	class Meta:
		verbose_name="Nota"
		verbose_name_plural="Notas"
	def __str__(self):
		return "{} {}".format(self. alumno, self.curso)


#Clase Matriculacion del profesor
class MatriculacionProfesor(models.Model):
	profesor = models.OneToOneField("Profesor", Profesor, related_name='matricula')
	curso = models.ForeignKey("Curso", Curso, related_name='matriculasProfesores')
	class Meta:
		verbose_name = "Matricula Profesor"
		verbose_name_plural = "Matricula de Profesores"
	def __str__(self):
		return "{} {}".format(self.profesor, self.curso)



#Clase Matriculacion del Alumno
class MatriculacionAlumno(models.Model):
	alumno = models.OneToOneField("Alumno", Alumno, related_name='matricula')
	curso = models.ForeignKey("Curso", Curso, related_name='matriculasAlumnos')
	class Meta:
		verbose_name = "Matricula de Alumno"
		verbose_name_plural = "Matriculas de Alumnos"
	def __str__(self):
		return "{} {}".format(self.alumno, self.curso)

