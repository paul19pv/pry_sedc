# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from anuarios.models import TemperaturaAire
from django.views.generic import ListView,FormView
from anuarios.forms import AnuarioForm
from anuarios import functions
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProcesarVariables(LoginRequiredMixin,FormView):
    template_name='anuarios/procesar_variable.html'
    form_class=AnuarioForm
    success_url='/anuarios/procesar'
    def post(self, request, *args, **kwargs):
        form=AnuarioForm(self.request.POST or None)
        save=False
        if form.is_valid():
            if self.request.is_ajax():
                datos=functions.calcular(form)
                template=functions.template(form.cleaned_data['variable'])
                exists=functions.verficar_anuario(form.cleaned_data['estacion']
                ,form.cleaned_data['variable'],form.cleaned_data['periodo'])
                functions.guardar_variable(datos,form)
                return render(request,template,{'datos':datos,'exists':exists})
        return self.render_to_response(self.get_context_data(form=form,save=True))
    def get_context_data(self, **kwargs):
        context = super(ProcesarVariables, self).get_context_data(**kwargs)
        return context
