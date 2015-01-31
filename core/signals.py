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
          view_log = log(entidad=l.entidad,  year=instance.year, month=instance.month, liberate=liberate_update, request = 0)
          view_log.save()
        else:
          print '{0} y {1} No se conocen'.format(l.entidad,view_entidad)
  except entidad.DoesNotExist:
    print e


post_save.connect(signal_post_save_liberar, sender=liberar)
