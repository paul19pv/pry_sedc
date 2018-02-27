# -*- coding: utf-8 -*-
from formato.models import Formato,Asociacion
from importacion.functions import (
    procesar_archivo_automatico,guardar_datos_automatico)
import daemon
import time
def iniciar_lectura():
    #time.sleep(10)
    while True:
        try:
            formatos=list(Formato.objects.filter(for_tipo='automatico'))
            for formato in formatos:
                consulta=list(Asociacion.objects.filter(for_id=formato.for_id))
                if len(consulta)>0:
                    estacion=consulta[0].est_id
                    registro=open('/tmp/sedc.txt','a')
                    registro.write(time.ctime()+': Lectura Iniciada - Estacion:'+str(estacion.est_codigo)+' Formato: '+str(formato.for_descripcion)+'\n')
                    registro.close()
                    archivo=open(formato.for_ubicacion+formato.for_archivo)
                    datos,variables=procesar_archivo_automatico(archivo,formato,estacion,formato.mar_id)
                    archivo.close()
                    if len(datos)>0:
                        guardar_datos_automatico(datos,variables)
                        registro=open('/tmp/sedc.txt','a')
                        registro.write(time.ctime()+': Información guardada Estacion:'+str(estacion.est_codigo)+'Formato:'+str(formato.for_descripcion)+'\n')
                        registro.close()

                    else:
                        registro=open('/tmp/sedc.txt','a')
                        registro.write(time.ctime()+': No existe nueva informacion para el Formato: '+str(formato.for_descripcion)+'\n')
                        registro.close()
                else:
                    registro=open('/tmp/sedc.txt','a')
                    registro.write(time.ctime()+': No existen formatos para iniciar la lectura'+'\n')
                    registro.close()
                    break
        except IOError as e:
            registro=open('/tmp/sedc.txt','a')
            registro.write(time.ctime()+': El archivo no existe'+'\n')
            registro.close()
            pass
        time.sleep(60)
def run(*args):
    with daemon.DaemonContext():
        iniciar_lectura()
