from django.db import models
from django.dispatch import receiver

# Create your models here.

class entidad(models.Model):
  # Entidades
  nombre = models.CharField( max_length=50)
  father = models.IntegerField(null=True,default=0, blank=True)

  def __unicode__(self):
    return self.nombre

  def is_father(self, entity):
    try:
      view_entidad = entidad.objects.get(id=entity.father)
      if self.pk == entity.father:
        return True
      else:
        return self.is_father(view_entidad)
    except entidad.DoesNotExist:
      return False

class liberar(models.Model):
  # Liberaciones
  entidad = models.ForeignKey(entidad)
  year = models.IntegerField()
  month = models.IntegerField()
  liberate = models.IntegerField()

class solicitud(models.Model):
  # Solicitudes
  entidad = models.ForeignKey(entidad)
  year = models.IntegerField()
  month = models.IntegerField()
  request = models.IntegerField()

class log(models.Model):
  # Conteo de solictudes vs. liberados
  entidad = models.ForeignKey(entidad)
  year = models.IntegerField()
  month = models.IntegerField()
  liberate = models.IntegerField()
  request = models.IntegerField(null=True,default=0, blank=True)
