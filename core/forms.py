# -*- coding: utf-8 -*-
from django.forms import *
from django import forms
from core.models import *
from core.signals import *

class liberateForm(ModelForm):
  entidad = forms.ModelChoiceField(queryset=entidad.objects.all())
  year = forms.CharField(max_length=4)
  month = forms.CharField(max_length=2)
  liberate = forms.CharField()

  class Meta:
    model = liberar

  def save(self):
    cleaned_data = self.cleaned_data
    super(liberateForm, self).save()

class entidadForm(ModelForm):
  nombre = forms.CharField()
  # father = forms.ModelChoiceField(queryset=entidad.objects.all(), required=False)

  def __init__(self, *args, **kwargs):
    super(entidadForm, self).__init__(*args, **kwargs)

    GROUP_ENTITY = [(g.pk,u'{}'.format(g.nombre))for g in entidad.objects.all()]
    self.fields['father'] = forms.ChoiceField(choices=GROUP_ENTITY, required=False )

  class Meta:
    model = entidad

  def clean(self):
    cleaned_data = super(entidadForm, self).clean()
    return cleaned_data

  def save(self):
    cleaned_data = self.cleaned_data
    if not self.instance.father:
      self.instance.father = None
    super(entidadForm, self).save()

class requestForm(ModelForm):
  def __init__(self, *args, **kwargs):
    simple = kwargs.pop('simple', False)
    super(requestForm, self).__init__(*args, **kwargs)

    if simple:
      self.fields['request'].required = False

  class Meta:
    model = solicitud

  def clean(self):
    cleaned_data = super(requestForm, self).clean()

    return cleaned_data

  def save(self):
    cleaned_data = self.cleaned_data
    try:
      view_entidad = entidad.objects.get(pk=self.instance.entidad.pk)
      return_log = view_entidad.posibles(self.instance.year, self.instance.month)
      posibles = return_log['posibles']
      if int(posibles) < int(self.instance.request):
        self._errors['request'] = self.error_class('No pidas mas de los que puedes')
    except entidad.DoesNotExist:
      self._errors['entidad'] = self.error_class('Entidad no existe')

    super(requestForm, self).save()