from django.shortcuts import render,redirect
from django.http import HttpResponse

from apps.main.forms import Usuario_From


# Create your views here.



def Principal(request):
	
	return render(request, 'base/Principal.html',{})



def Quienes_Somos(request):
	return render(request, 'Quienes_Somos/quienesSomos.html')



def Productos_Servicios(request):
	return render(request, 'Contenido/Productos_Servicios.html ')



def Contacto(request):
	return render(request, 'Contenido/Contactos.html ')



def Cursos(request):
	return render(request, 'Contenido/Cursos.html ')


def Proyectos(request):
	return render(request, 'Contenido/Proyectos.html ')



def Iniciar_Sesion(request):
	if request.method == 'POST':
		form = Usuario_From(request.POST)
		if form.is_valid():
			form.save()
		return redirect('Contenido:Inisiar_Sesion')
	else:
		form = Usuario_From()
	return render(request, 'Contenido/Inisiar_Sesion.html', {'form':form})






















