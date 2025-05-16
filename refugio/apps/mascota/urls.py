from django.conf.urls import url, include
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
 MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

from.import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#Funciones
   url(r'^crear$', mascota_view, name='mascota_crear'),
   url(r'^lista$', mascota_list , name='mascota_lista'),
   url(r'^modificar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_modificar'),
   url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
#Clases
   url(r'^nuevo$', MascotaCreate.as_view() , name='mascota_nuevo'),
   url(r'^listar$', MascotaList.as_view(), name='mascota_listar'),
   url(r'^editar/(?P<pk>\d+)/', MascotaUpdate.as_view(), name='mascota_editar'),
   url(r'^delete/(?P<pk>\d+)/', MascotaDelete.as_view(), name='mascota_delete'),     
]
