from django.shortcuts import HttpResponse
from django.shortcuts import render

def leer_persona(request):
    return render(request, 'persona.html')

def leer_datosdecontacto(request):
    return render(request, 'datosdecontacto.html')

def leer_intereser(request):
    return render(request, 'intereses.html')

def index(request):
    return render(request, 'index.html')

