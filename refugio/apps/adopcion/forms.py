from django import forms
from django.core.exceptions import ValidationError
from apps.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos':'Apellidos',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'domicilio':'Domicilio',
        }
        widgets = {
            
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.NumberInput(attrs={'class':'form-control'}),
            'telefono':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.Textarea(attrs={'class':'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('Por favor escribe tu nombre')
        return nombre

    def clean_apellidos(self):
        apellidos = self.cleaned_data.get('apellidos')
        if not apellidos:
            raise forms.ValidationError('Por favor escribe tu apellido')
        return apellidos

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if not edad or edad < 18:
            raise forms.ValidationError('Debes ser mayor de edad para adoptar una mascota')
        return edad

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono or len(str(telefono)) < 10 :
            raise forms.ValidationError('El numero telefonico debe contener 10 digitos')
        return telefono

    def clean_domicilio(self):
        domicilio = self.cleaned_data.get('domicilio')
        if not domicilio:
            raise forms.ValidationError('Por favor escribe tu direccion')
        return domicilio

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [
            'numero_mascotas',
            'razones',
        ]
        labels = {
            'numero_mascotas': 'Numero de mascotas',
            'razones':'Razones para adoptar',
        }
        widgets = {            
            'numero_mascotas':forms.NumberInput(attrs={'class':'form-control'}),
            'razones':forms.Textarea(attrs={'class':'form-control'}),
        }