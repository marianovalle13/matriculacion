from django.shortcuts import render, redirect
from .models import *
# Create your views here.

#funcion curso
def lolito(request):
	traer = Alumno.objects.all()
	return render(request, 'principal.html', {'traer_alumnos': traer})
	
def cargar_nota(request, lolo, pinke):
	nota = request.POST["nota"]
	alumno = Alumno.objects.get(id=lolo)
	curso = Curso.objects.get(id=pinke)
	nueva_nota = Nota(valor=nota, alumno=alumno, curso=curso)
	nueva_nota.save()
	return redirect("papito")
