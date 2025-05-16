
#from django.urls import include
from.import views

#from django.urls import path
from django.conf.urls import url, include
#from django.contrib.auth.decorators import login_required

from apps.adopcion.views import index_adopcion, adopcion_view,adopcion_list, adopcion_modificar, adopcion_delete, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete
urlpatterns = [
   #url(r'^index$', index_adopcion)
   #path('',views.index_adopcion,name='index_adopcion'),
#Clases
    url(r'^index$',(index_adopcion)),
    url(r'^solicitud/listar$',(SolicitudList.as_view()), name='solicitud_listar'),
    url(r'^solicitud/crear$',(SolicitudCreate.as_view()), name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)/',(SolicitudUpdate.as_view()), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)/',(SolicitudDelete.as_view()), name='solicitud_eliminar'),
#Funciones
   url(r'^solicitud/nueva$', adopcion_view, name='solicitud_nueva'),
   url(r'^solicitud/lista$', adopcion_list , name='solicitud_lista'),
   url(r'^solicitud/modificar/(?P<id_solicitud>\d+)/$', adopcion_modificar, name='solicitud_modificar'),
   url(r'^solicitud/delete/(?P<id_solicitud>\d+)/$', adopcion_delete, name='solicitud_delete'),
]