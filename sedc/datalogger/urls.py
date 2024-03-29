from django.conf.urls import url
from datalogger import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'datalogger/$',views.DataloggerList.as_view(),name='datalogger_index'),
    url(r'datalogger/(?P<page>[0-9]+)/$',views.DataloggerList.as_view(),name='datalogger_index'),
    url(r'datalogger/create/$', views.DataloggerCreate.as_view(), name='datalogger_create'),
    url(r'datalogger/detail/(?P<pk>[0-9]+)/$', views.DataloggerDetail.as_view(), name='datalogger_detail'),
    url(r'datalogger/edit/(?P<pk>[0-9]+)/$', views.DataloggerUpdate.as_view(), name='datalogger_update'),
    url(r'datalogger/(?P<pk>[0-9]+)/delete/$', views.DataloggerDelete.as_view(), name='datalogger_delete'),


]
