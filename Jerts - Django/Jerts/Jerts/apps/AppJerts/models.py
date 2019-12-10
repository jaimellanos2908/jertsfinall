from django.db import models
from django.forms import ModelForm


# Create your models here.

class Contacto(models.Model):
	Nombre = models.CharField(max_length=200)
	Email = models.CharField(max_length=150)
	Telefono = models.CharField(max_length=20)
	Descripcion = models.TextField('Descripción', blank=True)

	def __str__(self):
		return self.Nombre


