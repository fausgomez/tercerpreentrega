from django.urls import path

from appfaustinogomez.views import (
    leer_persona, 
    leer_datosdecontacto, 
    leer_intereser, 
    index,
    persona_formulario,
    datos_formulario,
    intereses_formulario,
    busqueda_dni,
    buscar_dni,
    busqueda_email,
    buscar_email,
    busqueda_intereses,
    buscar_intereses,
)

urlpatterns = [
    path("persona/", leer_persona, name='Persona'),
    path("datosdecontacto/", leer_datosdecontacto, name= 'DatosDeContacto'),
    path("intereses/", leer_intereser, name= 'Intereses'),
    path("personaFormulario", persona_formulario, name='persona_formulario'),
    path("datosFormulario", datos_formulario, name='datos_formulario'),
    path("interesesFormulario", intereses_formulario, name='intereses_formulario'),
    path("busquedaPersona", busqueda_dni, name="busqueda_persona"),
    path("buscarDni", buscar_dni, name='buscar_dni'),
    path("busquedaEmail", busqueda_email, name="busqueda_email"),
    path("buscarEmail", buscar_email, name="buscar_email"),
    path("busqeudaIntereses", busqueda_intereses, name="busqueda_intereses"),
    path("buscarIntereses", buscar_intereses, name="buscar_intereses"),
    path("", index, name= 'index'),
]