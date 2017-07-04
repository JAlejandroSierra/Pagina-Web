from django.conf.urls import url, include 
from apps.main.views import  Principal, Quienes_Somos, Productos_Servicios, Cursos, Contacto, Proyectos, Iniciar_Sesion


urlpatterns = [
	
    url(r'^', Principal, name='Principal'),
    url(r'^', Quienes_Somos, name='Quienes_Somos'),
    url(r'^', Productos_Servicios, name='Productos_Servicios'),
    url(r'^', Cursos, name='Cursos'),
    url(r'^', Contacto, name='Contacto'),
    url(r'^', Proyectos, name='Proyectos'),
    url(r'^', Iniciar_Sesion, name='Iniciar_Sesion'),

]