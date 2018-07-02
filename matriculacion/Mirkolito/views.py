from django.shortcuts import render

# Create your views here.
#funcion curso
def cursos(request):
	profe = Profesor.objects.get(usuario=request.user)
	return render(request, "curso.html", {"cursos_del_profe":Curso.objects.filter(id__in=MatriculaProfesor.objects.filter(profesor=profe))})