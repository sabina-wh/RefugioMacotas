from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm
from django.contrib.messages.views import SuccessMessageMixin




def index_adopcion(request):
    return HttpResponse("Index de la app Adopcion")

def adopcion_view(request):
    if request.method == 'POST':
        form2 = PersonaForm(request.POST)
        form = SolicitudForm(request.POST)
        if form.is_valid() and form2.is_valid():
            persona = form2.save()
            solicitud = form.save(commit=False)
            solicitud.persona = persona
            solicitud.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Nueva solicitud agregada')
            return redirect('solicitud_lista')
    else :
        form2 =PersonaForm()
        form =SolicitudForm()
    return render(request,'adopcion/solicitud_form.html',{'form2':form2, 'form':form})

def adopcion_list(request):
    solicitudes = Solicitud.objects.all()
    personas = Persona.objects.all()
    return render(request, 'adopcion/solicitud_listar.html',{'solicitudes': solicitudes, 'personas': personas})

def adopcion_modificar(request, id_solicitud):
    solicitudes = Solicitud.objects.all()
    persona = solicitud.persona
    if request.method == 'GET':
        form2 = PersonaForm(instance = persona)
        form = SolicitudForm(instance = solicitud)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, 'Tu solicitud ha ido actualizada')
        return redirect('solicitud_lista')
    else:
        form2 = PersonaForm(instance=persona)
        form = SolicitudForm(instance=solicitud)
    return render(request, 'adopcion/solicitud_form.html', {'form':form, 'form2':form2})

def adopcion_delete(request, id_solicitud):
    solicitudes = Solicitud.objects.all()
    if request.method == 'POST':
        solicitud.delete()
        messages.success(request, 'La solicitud fue eliminada.')
        return redirect('solicitud_lista')  # Redirige a la lista de solicitudes de adopción
    return render(request, 'adopcion/solicitud_delete.html', {'solicitud': solicitud})


class SolicitudList(ListView):
    model = Solicitud
    template_name='adopcion/solicitud_list.html'

class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    #Guardar el registro de persona que esta relacionado con la solicitud
    second_form_class = PersonaForm
    success_url = reverse_lazy('solicitud_listar')
#sobreescribi los metodos basados en clase
    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            #NOs aseguramos que los formularios esten en el contexto
            if 'form' not in context:
                context['form'] = self.form_class(self.request.POST)
            if 'form2' not in context:
                context['form2'] = self.second_form_class(self.request.POST)
        else:
            if 'form' not in context:
                context['form'] = self.form_class()
            if 'form2' not in context:
                context['form2'] = self.second_form_class()
        return context


#Guardar y  crear la relacion 
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)#obtenemos los datos modelo del formulario, luego puedes agregar tus datos adicionales y guardarlos.
            solicitud.persona = form2.save()
            solicitud.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Tu solicitud ha sido agregada')
            return HttpResponseRedirect(self.get_success_url())            
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model = Persona
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('solicitud_listar')


    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='La solicitud fue modificada')
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopcion/solicitud_delete.html'
    success_url = reverse_lazy('solicitud_listar')

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, 'la solicitud fue eliminada')
        return super().delete(request, *args, **kwargs)
        #Usa delete() en lugar de form_valid() en un DeleteView, ya que no hay formulario como tal.

