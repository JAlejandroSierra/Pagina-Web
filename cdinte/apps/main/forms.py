from django import forms

from apps.main.models import Usuario


class Usuario_From(forms.ModelForm):

	class Meta:
		model = Usuario

		fields = [

			'Nombre',
			'Apellido',
			'Correo',
			'Sexo',
			'FechaNacimiento',
		]
		labels = {

			'Nombre': 'NOMBRE',
			'Apellido': 'APELLIDO',
			'Correo': 'CORREO',
			'Sexo': 'SEXO',
			'FechaNacimiento': 'FECHA DE NACIMIENTO',
		}

		widgets = {
			'Nombre': forms.TextInput(attrs={'class':'form-contro'}),
			'Apellido': forms.TextInput(attrs={'class':'form-contro'}),
			'Correo': forms.TextInput(attrs={'class':'form-contro'}),
			'Sexo': forms.TextInput(attrs={'class':'form-contro'}),
			'FechaNacimiento':  forms.TextInput(attrs={'class':'form-contro'}),





		}