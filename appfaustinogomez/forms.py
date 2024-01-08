from django import forms

class PersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.DecimalField(max_digits=10, decimal_places=0)

class DatosFormulario(forms.Form):
    telefono = forms.DecimalField(max_digits=12, decimal_places=0)
    email = forms.EmailField()
    direccion = forms.CharField(max_length=20)

class InteresesFormulario(forms.Form):
    autos = forms.BooleanField(required=False)
    animales = forms.BooleanField(required=False)
    medioambiente = forms.BooleanField(required=False)
    viajes = forms.BooleanField(required=False)




