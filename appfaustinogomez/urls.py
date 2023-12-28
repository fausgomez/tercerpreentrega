from django.urls import path

from appfaustinogomez.views import leer_persona, leer_datosdecontacto, leer_intereser

urlpatterns = [
    path("persona/", leer_persona),
    path("datosdecontacto/", leer_datosdecontacto),
    path("intereses/", leer_intereser),
]