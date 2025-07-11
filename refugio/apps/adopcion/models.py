from django.db import models
# Un modelo Django es una descripcion de los datos en la BD representada como codigo Python
# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=70)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()#incluye validacion automatica para email valido
	domicilio = models.TextField()

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellidos)

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True,on_delete=models.CASCADE)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()