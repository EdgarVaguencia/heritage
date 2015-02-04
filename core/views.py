from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import *
from core.forms import *

# Create your views here.
@csrf_protect
def entidadView(request):

  list_errors = []
  form_entidad = entidadForm()

  if request.method == 'POST':
    form_entidad = entidadForm(request.POST)
    if form_entidad.is_valid():
      form_entidad.save()
    
    for field, errors in form_entidad.errors.items():
      list_errors.append({
          'field': field,
          'errors': errors
      })

  model_list = entidad.objects.all()

  return render_to_response(
    'entidad.html',
    {
      'list' : model_list,
      'form' : form_entidad,
      'error' : list_errors,
    },
    context_instance = RequestContext(request)
  )

@csrf_protect
def liberateView(request):

  if request.method == 'POST':
    form_liberate = liberateForm(request.POST)
    if form_liberate.is_valid():
      form_liberate.save()

  model_list = liberar.objects.all()
  form_liberate = liberateForm()

  return render_to_response(
    'liberar.html',
    {
      'list' : model_list,
      'form' : form_liberate
    },
    context_instance = RequestContext(request)
  )

@csrf_protect
def requestView(request,type_request=None):

  form_request = None
  _form_request = None
  posibles = None

  if request.method == 'POST':
    form_request = requestForm(request.POST,simple=True)
    if type_request == "1": # Busqueda de posibles a solicitar
      _form_request = form_request
      try:
        view_entidad = entidad.objects.get(pk=request.POST['entidad'])
        return_log = view_entidad.posibles(request.POST['year'], request.POST['month'])
        posibles = return_log['posibles']
      except entidad.DoesNotExist:
        print 'Esa Entidad ni existe'
    if type_request == "2":
      _form_request = requestForm(request.POST)
      if _form_request.is_valid():
        _form_request.save()
  else:
    form_request = requestForm
    _form_request = requestForm

  model_list = solicitud.objects.all()

  return render_to_response(
    'solicitar.html',
    {
      'form' : form_request,
      'form2' : _form_request,
      'posibles' : posibles,
      'list' : model_list,
    },
    context_instance = RequestContext(request)
  )

