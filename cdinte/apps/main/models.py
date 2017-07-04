from django.db import models


class Usuario(models.Model):
	Nombre = models.CharField(max_length=50)
	Apellido = models.CharField(max_length=50)
	Correo = models.CharField(max_length=50)
	Sexo = models.CharField(max_length=10)
	FechaNacimiento = models.DateField()


