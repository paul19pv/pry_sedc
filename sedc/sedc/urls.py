"""sedc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^',include('home.urls',namespace='home')),
    url(r'^',include('reportes.urls',namespace='reportes')),
    url(r'^',include('datalogger.urls',namespace='datalogger')),
    url(r'^',include('estacion.urls',namespace='estacion')),
    url(r'^',include('variable.urls',namespace='variable')),
    url(r'^',include('formato.urls',namespace='formato')),
    url(r'^',include('medicion.urls',namespace='medicion')),
    url(r'^',include('vacios.urls',namespace='vacios')),
    url(r'^',include('frecuencia.urls',namespace='frecuencia')),
    url(r'^',include('importacion.urls',namespace='importacion')),
    url(r'^',include('marca.urls',namespace='marca')),
    url(r'^',include('validacion.urls',namespace='validacion')),
    url(r'^',include('anuarios.urls',namespace='anuarios')),
    url(r'^',include('sensor.urls',namespace='sensor')),
    url(r'^',include('instalacion.urls',namespace='instalacion')),
    url(r'^',include('bitacora.urls',namespace='bitacora')),
    url(r'^',include('cruce.urls',namespace='cruce')),
    url(r'^',include('registro.urls',namespace='registro')),
    url('^', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
