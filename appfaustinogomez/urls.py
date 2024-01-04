from django.urls import path

from appfaustinogomez.views import leer_persona, leer_datosdecontacto, leer_intereser, index

urlpatterns = [
    path("persona/", leer_persona, name='Persona'),
    path("datosdecontacto/", leer_datosdecontacto, name= 'DatosDeContacto'),
    path("intereses/", leer_intereser, name= 'Intereses'),
    path("", index, name= 'index'),
]