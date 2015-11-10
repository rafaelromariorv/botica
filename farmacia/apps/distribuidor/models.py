from django.db import models

class Distribuidor(models.Model):
	codigo = models.IntegerField(max_length=10, blank=True, default=1, unique=True)
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=60)
	ruc = models.IntegerField(max_length=11)
	direccion = models.CharField(max_length=60)

	def __unicode__(self):
		return self.nombre