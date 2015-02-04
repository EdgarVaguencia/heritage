# -*- coding: utf-8 -*-
from django.db.models.signals import pre_save, post_save
from core.models import *

def signal_post_save_liberar(sender, instance, **kwargs):
  try:
    view_entidad = entidad.objects.get(id=instance.entidad.pk)
    try:
      view_log = log.objects.get(entidad=view_entidad, year=instance.year, month=instance.month)
      liberate_update = view_log.liberate + instance.liberate
      view_log.liberate = liberate_update
      view_log.save()
    except log.DoesNotExist:
      view_log = log(entidad=instance.entidad, year=instance.year, month=instance.month, liberate=instance.liberate, request=0)
      view_log.save()

    for l in log.objects.exclude(entidad=view_entidad):
      if (l.year == instance.year and l.month <= instance.month) or (l.year < instance.year):
        if view_entidad.is_father(l.entidad):
          liberate_update = l.liberate + instance.liberate
          view_log = log(entidad=l.entidad, year=instance.year, month=instance.month, liberate=liberate_update, request = 0)
          view_log.save()
        else:
          print '{0} y {1} No se conocen'.format(l.entidad,view_entidad)
  except entidad.DoesNotExist:
    print 'Estamos en señales y la entidad no existe en liberar'

def signal_post_save_solicitar(sender, instance, **kwargs):
  try:
    view_entidad = entidad.objects.get(id=instance.entidad.pk)
    return_log = view_entidad.posibles(instance.year, instance.month)
    view_log = return_log['log']
    request_update = view_log.request + instance.request
    view_log.request = request_update
    view_log.save()
    if not instance.entidad.pk == view_log.entidad.pk:
      try:
        _view_log = log.objects.get(entidad=instance.entidad, year=view_log.year, month=view_log.month)
        request_update = _view_log.request + instance.request
        _view_log.request = request_update
      except log.DoesNotExist:
        _view_log = log(entidad=instance.entidad, year=view_log.year, month=view_log.month, liberate=0, request=instance.request)
      _view_log.save()
    for l in log.objects.filter(entidad=view_log.entidad): # Mas estradas de la entidad en el futuro
      if (l.year == view_log.year and l.month > view_log.month) or (l.year > view_log.year):
        request_update = l.request + instance.request
        l.request = request_update
        l.save()
  except entidad.DoesNotExist:
    print 'Estamos en señales y la entidad no existe al solicitar'

# Liberar
post_save.connect(signal_post_save_liberar, sender=liberar)

# Solicitar
post_save.connect(signal_post_save_solicitar, sender=solicitud)
