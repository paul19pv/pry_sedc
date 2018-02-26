# -*- coding: utf-8 -*-

#from django import forms
from django.forms import ModelForm
from formato.models import Formato, Clasificacion,Asociacion
from django import forms
class FormatoSearchForm(ModelForm):
    lista=[]
    for_descripcion = forms.CharField(
        max_length=200,
        required=False,
        help_text='Puede usar una o varias palabras',
        label='Descripción'
    )
    class Meta:
        model=Formato
        fields=['for_descripcion']
    def filtrar(self,form):
        for_descripcion=form.cleaned_data['for_descripcion']
        if for_descripcion:
            lista=Formato.objects.filter(
                for_descripcion__icontains=for_descripcion
            )
        else:
            lista=Formato.objects.all()
        return lista

    def cadena(self,form):
        keys=form.cleaned_data.keys()
        string=str("?")
        i=1
        for item in keys:
            if i<len(keys):
                string+=item+"="+str(form.cleaned_data[item])+"&"
            else:
                string+=item+"="+str(form.cleaned_data[item])
            i+=1
        return string

class ClasificacionSearchForm(ModelForm):
    lista=[]
    class Meta:
        model=Clasificacion
        fields=['var_id','for_id']
    def filtrar(self,form):
        for_id=form.cleaned_data['for_id']
        var_id=form.cleaned_data['var_id']
        if var_id and for_id:
            lista=Clasificacion.objects.filter(
                var_id=var_id
            ).filter(
                for_id=for_id
            )
        elif var_id is None and for_id:
            lista=Clasificacion.objects.filter(
                for_id=for_id
            )
        elif for_id is None and var_id:
            lista=Clasificacion.objects.filter(
                var_id=var_id
            )
        elif var_id is None and for_id is None:
            lista=Clasificacion.objects.all()
        else:
            lista=Clasificacion.objects.all()
        return lista

    def cadena(self,form):
        keys=form.cleaned_data.keys()
        string=str("?")
        i=1
        for item in keys:
            if i<len(keys):
                string+=item+"="+str(form.cleaned_data[item])+"&"
            else:
                string+=item+"="+str(form.cleaned_data[item])
            i+=1
        return string
class AsociacionSearchForm(ModelForm):
    lista=[]
    class Meta:
        model=Asociacion
        fields=['est_id','for_id']
    def filtrar(self,form):
        for_id=form.cleaned_data['for_id']
        est_id=form.cleaned_data['est_id']
        if est_id and for_id:
            lista=Asociacion.objects.filter(
                est_id=est_id
            ).filter(
                for_id=for_id
            )
        elif est_id is None and for_id:
            lista=Asociacion.objects.filter(
                for_id=for_id
            )
        elif for_id is None and est_id:
            lista=Asociacion.objects.filter(
                est_id=est_id
            )
        elif est_id is None and for_id is None:
            lista=Asociacion.objects.all()
        else:
            lista=Asociacion.objects.all()
        return lista

    def cadena(self,form):
        keys=form.cleaned_data.keys()
        string=str("?")
        i=1
        for item in keys:
            if i<len(keys):
                string+=item+"="+str(form.cleaned_data[item])+"&"
            else:
                string+=item+"="+str(form.cleaned_data[item])
            i+=1
        return string
