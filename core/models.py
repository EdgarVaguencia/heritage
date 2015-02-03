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
      print 'no se conocen'
      return False

  def is_father_level(self, entity, level=0):
    try:
      view_entidad = entidad.objects.get(id=entity.father)
      level = level + 1
      if self.pk == entity.father:
        return level
      else:
        return self.is_father_level(view_entidad, level)
    except entidad.DoesNotExist:
      print 'no se conocen'
      return level


  def posibles(self, year, month):
    posibles = 0
    actual_in_log = True
    try: # Buscamos los disponibles de la entidad solicitada
      flag = 100
      for l in log.objects.filter(entidad=self.pk):
        if( int(l.year) == int(year) and int(l.month) <= int(month) ) or ( int(l.year) < int(year) ):
          if int(l.year) > int(year) and int(l.month) < int(month):
            formula = int(int(l.year) - int(year)) - int(int(l.month) - int(month))
          else:
            formula = int(int(l.year) - int(year)) + int(int(l.month) - int(month))
          if formula < flag or formula == 0:
            flag = formula
            posibles = l.liberate - l.request
    except log.DoesNotExist:
      actual_in_log = False

    if not actual_in_log or posibles <= 0: # Buscamos en sus padres tienen disponible
      flag = 100
      level = 100
      for l in log.objects.exclude(entidad=self.pk):
        view_entidad = entidad.objects.get(pk=l.entidad.pk)
        if view_entidad.is_father(self):
          father_level = view_entidad.is_father_level(self)
          if( int(l.year) == int(year) and int(l.month) <= int(month) ) or ( int(l.year) < int(year) ):
            if int(l.year) > int(year) and int(l.month) < int(month):
              formula = int(int(l.year) - int(year)) - int(int(l.month) - int(month))
            else:
              formula = int(int(l.year) - int(year)) + int(int(l.month) - int(month))
            if (formula < flag or formula == 0) and father_level <= level:
              flag = formula
              level = father_level
              posibles = l.liberate - l.request

    return posibles

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
