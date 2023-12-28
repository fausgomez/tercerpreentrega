from django.shortcuts import HttpResponse
from django.shortcuts import render

def leer_persona(request):
    return HttpResponse("Vista Persona")

def leer_datosdecontacto(request):

    contexto = {
        "nombre" : "Pepe",
        "apellido" : "Rodriguez",
        "datos" : ['1122334455', 'pepe@gmail.com', 'Av. siempreviva 1234']
    }

    return  render(request, 'plantilla.html', contexto)

def leer_intereser(request):
    return HttpResponse("Vista intereses")

def index(request):
    return render(request, 'index.html')

