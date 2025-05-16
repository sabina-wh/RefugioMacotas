from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
	return render(request, 'mascota/index.html')

def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.add_message(request=request, level=messages.SUCCESS, message='La mascota ha sido agregada')
			return redirect('mascota_lista')
	else :
		form =MascotaForm()
	return render(request,'mascota/mascota_form.html',{'form':form})

	

def mascota_list(request):
	mascota = Mascota.objects.all().order_by('id')
	contexto = { 'mascotas':mascota}
	return render(request, 'mascota/mascota_listar.html', contexto)

def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
			messages.add_message(request=request, level=messages.SUCCESS, message='Tus modificacciones han sido guardadas')
		return redirect('mascota_lista')
	return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		messages.add_message(request=request, level=messages.ERROR, message='La mascota ha sido eliminada')
		return redirect('mascota_lista')
	return render(request, 'mascota/mascota_eliminar.html', {'mascota':mascota})


class MascotaList(ListView):
	model = Mascota
	template_name = 'mascota/mascota_list.html'
	ordering = ['id']

class MascotaCreate(SuccessMessageMixin, CreateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota_listar')

	def form_valid(self, form):
		messages.success(self.request, 'Nueva mascota agregada')
		return super().form_valid(form)

class MascotaUpdate(SuccessMessageMixin, UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota_listar')

	def form_valid(self, form):
		messages.success(self.request, 'la mascota ha sido actualizada')
		return super().form_valid(form);

class MascotaDelete(DeleteView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota_listar')
        
    def delete(self, request, *args, **kwargs):
        messages.error(self.request, 'la mascota fue eliminada')
        return super().delete(request,*args, **kwargs)
