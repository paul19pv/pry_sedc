from django.conf.urls import url
from importacion import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns=[
    url(r'^importacion/$',views.ImportacionList.as_view(),name='importacion_index'),
    url(r'^importacion/(?P<page>[0-9]+)/$',views.ImportacionList.as_view(),name='importacion_index'),
    url(r'importacion/create/$', views.ImportacionCreate.as_view(), name='importacion_create'),
    url(r'importacion/detail/(?P<pk>[0-9]+)/$', views.ImportacionDetail.as_view(), name='importacion_detail'),
    url(r'importacion/guardar/(?P<imp_id>[0-9]+)/$', views.guardar_archivo, name='importacion_guardar'),
    url(r'importacion/(?P<pk>[0-9]+)/delete/$', views.ImportacionDelete.as_view(), name='importacion_delete'),
    url(r'importacion/lectura/$', views.lectura_automatica, name='lectura'),
    url(r'^ajax/formatos',views.lista_formatos,name='formatos')
]
