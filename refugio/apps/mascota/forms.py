from django import forms
from django.core.exceptions import ValidationError
from apps.mascota.models import Mascota
from apps.adopcion.models import Persona
import datetime
#from .models import Image

class MascotaForm(forms.ModelForm):
    
    class Meta:
    	model = Mascota 

    	fields = [
    		'nombre',
    		'sexo',
    		'edad_aproximada',
    		'fecha_rescate',
    		'persona',
    		'vacuna',
            'imagen',
    	]
    	labels= {
    		'nombre': 'Nombre',
    		'sexo': 'Sexo',
    		'edad_aproximada': 'Edad aproximada',
    		'fecha_rescate': 'Fecha de rescate',
    		'persona': 'Adoptante',
    		'vacuna': 'Vacunas',
            'imagen': 'Imagen',
    	}
    	widgets = {
    		'nombre': forms.TextInput(attrs={'class':'form-control'}) ,       
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
    		'edad_aproximada': forms.NumberInput(attrs={'class':'form-control'}),
    		'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
    		'persona': forms.Select(attrs={'class':'form-control form-select'}), 
            'vacuna': forms.CheckboxSelectMultiple(),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    	}

    def clean_nombre(self):
        nombremascota = self.cleaned_data.get('nombre')
        if not nombremascota:
            raise forms.ValidationError('Por favor, ingresa el nombre de la mascota')
        return nombremascota

    def clean_sexo(self):
        sexo = self.cleaned_data.get('sexo')
        valores_validos = ['macho', 'hembra']
        if not sexo or sexo.lower() not in valores_validos:
            raise forms.ValidationError('Por favor, ingresa un valor válido para el sexo: Macho o Hembra')
        return sexo

    def clean_edad_aproximada(self):
        edad_aproximada = self.cleaned_data.get('edad_aproximada')
        if not edad_aproximada:
            raise forms.ValidationError('Por favor, ingresa la edad aproximada de la mascota')
        return edad_aproximada  

    def clean_fecha_rescate(self):
        fecha_rescate = self.cleaned_data.get('fecha_rescate')
        if fecha_rescate > datetime.date.today():
            raise ValidationError("Fecha incorrecta : no puede ser mayor al dia de hoy")
        return fecha_rescate

    def clean_persona(self):
        persona = self.cleaned_data.get('persona')
        if not persona:
            raise forms.ValidationError('Por favor,selecciona un adoptante')
        return persona

    def clean_vacuna(self):
        vacuna = self.cleaned_data.get('vacuna')
        if not vacuna:
            raise forms.ValidationError('Por favor,elige una vacuna')
        return vacuna

    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['persona'].choices = [(" ","Selecciona")]+[(persona.id,persona.nombre) for persona in Persona.objects.all()]


