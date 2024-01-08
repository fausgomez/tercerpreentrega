from django.urls import path

from appfaustinogomez.views import (
    leer_persona, 
    leer_datosdecontacto, 
    leer_intereser, 
    index,
    persona_formulario,
    datos_formulario,
    intereses_formulario,
)

urlpatterns = [
    path("persona/", leer_persona, name='Persona'),
    path("datosdecontacto/", leer_datosdecontacto, name= 'DatosDeContacto'),
    path("intereses/", leer_intereser, name= 'Intereses'),
    path("personaFormulario", persona_formulario, name='persona_formulario'),
    path("datosFormulario", datos_formulario, name='datos_formulario'),
    path("interesesFormulario", intereses_formulario, name='intereses_formulario'),
    path("", index, name= 'index'),
]