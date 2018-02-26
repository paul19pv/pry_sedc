from django.conf.urls import url
from reportes import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^reportes/anuario/$', views.ReportesAnuario.as_view(), name='anuario'),
    url(r'^reportes/consultas/$',views.ConsultasPeriodo.as_view(),name='consultas_periodo'),
    url(r'^reportes/comparacion/$',views.ComparacionValores.as_view(),name='comparacion_reporte'),
    url(r'reportes/datos_horarios/(?P<est_id>[0-9]+)/(?P<var_id>[0-9]+)/(?P<fec_ini>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})/(?P<fec_fin>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})/$',views.datos_json_horarios,name='horarios'),

]
