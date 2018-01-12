# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from importacion.models import Importacion
from vacios.models import Vacios
from django.views.generic import ListView,FormView
from django.views.generic.detail import DetailView
from django.http import JsonResponse

from django.http import HttpResponseRedirect
#from django.shortcuts import render
from importacion.forms import UploadFileForm,VaciosForm
from importacion.functions import (consultar_formatos,guardar_datos,
    procesar_archivo,guardar_vacios)

from django.db import transaction


class ImportacionList(ListView):
    model=Importacion
    def get_context_data(self, **kwargs):
        context = super(ImportacionList, self).get_context_data(**kwargs)
        return context

class ImportacionDetail(DetailView):
    model=Importacion

class ImportarArchivo(FormView):
    template_name='importacion/importacion_form.html'
    form_class=UploadFileForm
    success_url='/importacion/importar/'
    informacion={}
    def post(self, request, *args, **kwargs):
        form=UploadFileForm(request.POST, request.FILES)
        #form=UploadFileForm(self.request.POST)
        if form.is_valid():
            self.informacion=procesar_archivo(request.FILES['archivo'],form,request)
            if ((self.informacion['valid'] and
                not form.cleaned_data['sobreescribir']) or
                (not self.informacion['valid'] and
                form.cleaned_data['sobreescribir'])):
                if self.informacion['vacio']:
                    self.informacion.update({'form':VaciosForm()})
                return render(request, 'importacion/confirmacion.html',self.informacion)
            '''elif not self.informacion['valid'] and form.cleaned_data['sobreescribir']:
                if self.informacion['vacio']:
                    self.informacion.update({'form':VaciosForm()})
                return render(request, 'importacion/confirmacion.html',self.informacion)'''
        return self.render_to_response(self.get_context_data(form=form))
    def get_context_data(self, **kwargs):
        context = super(ImportarArchivo, self).get_context_data(**kwargs)
        if len(self.informacion)>0:
            context['message']=self.informacion['message']
        return context

class GuardarArchivo(FormView):
    template_name='importacion/confirmacion.html'
    form_class=VaciosForm
    success_url='/importacion/'
    def post(self, request, *args, **kwargs):
        form=VaciosForm(request.POST or None)

        if form.is_valid():
            guardar_vacios(request,form.cleaned_data['observacion'])
        with transaction.atomic():
            guardar_datos(request)

        return render(request, 'importacion/mensaje.html',{'mensaje':'Informacion Cargada'})

        #return self.render_to_response(self.get_context_data(form=form))



def guardar_archivo(request):
    sobreescribir=request.GET.get('sobreescribir',None)
    with transaction.atomic():
        guardar_datos(sobreescribir)
    return render(request, 'importacion/mensaje.html',{'mensaje':'Informacion Cargada'})

#lista de formatos por estacion y datalogger
def lista_formatos(request):
    mar_id=request.GET.get('datalogger',None)
    datos=consultar_formatos(mar_id)
    data={
        'datos':datos,
    }
    return JsonResponse(datos)

'''def importar_archivo(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=procesar_archivo(request.FILES['archivo'],form,request)

            if informacion['valid'] and not form.cleaned_data['sobreescribir']:
                return render(request, 'importacion/confirmacion.html',informacion)
            elif not informacion['valid'] and form.cleaned_data['sobreescribir']:
                return render(request, 'importacion/confirmacion.html',informacion)
            elif informacion['valid'] and form.cleaned_data['sobreescribir']:
                context={
                    'form':form,
                    'message':informacion['message'],
                }
                return render(request, 'importacion/importacion_form.html',context)
            else:
                context={
                    'form':form,
                    'message':informacion['message'],
                }
                return render(request, 'importacion/importacion_form.html',context)
    else:
        form = UploadFileForm()
    return render(request, 'importacion/importacion_form.html', {'form': form})'''