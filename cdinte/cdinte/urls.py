"""cdinte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Principal', include('apps.main.urls',namespace="Principal")),
    url(r'^Quienes_Somos', include('apps.main.urls',namespace="Quienes_Somos")),
    url(r'^Productos_Servicios', include('apps.main.urls',namespace="Productos_Servicios")),
    url(r'^Cursos', include('apps.main.urls',namespace="Cursos")),
    url(r'^Contacto', include('apps.main.urls',namespace="Contacto")),
    url(r'^Proyectos', include('apps.main.urls',namespace="Proyectos")),
    url(r'^Iniciar_Sesion', include('apps.main.urls',namespace="Iniciar_Sesion")),

    
]
