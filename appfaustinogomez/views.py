from django.shortcuts import HttpResponse
from django.shortcuts import render

from appfaustinogomez.models import Persona
from appfaustinogomez.forms import PersonaFormulario
from appfaustinogomez.models import DatosDeContacto
from appfaustinogomez.forms import DatosFormulario
from appfaustinogomez.models import Intereses
from appfaustinogomez.forms import InteresesFormulario

def leer_persona(request):
    return render(request, 'persona.html')

def leer_datosdecontacto(request):
    return render(request, 'datosdecontacto.html')

def leer_intereser(request):
    return render(request, 'intereses.html')

def index(request):
    return render(request, 'index.html')



def persona_formulario(request):

    if request.method == "POST":

        formulario = PersonaFormulario(request.POST)

        print(f" is valid: {formulario.is_valid}")
        if formulario.is_valid():

            datos = formulario.cleaned_data

            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            dni = datos.get("dni")

            persona = Persona(nombre=nombre, apellido=apellido, dni=dni)

            persona.save()

            return render(request, 'index.html') 
        
    else:
        formulario = PersonaFormulario()


    return render(request, 'persona_formulario.html', {"formulario": formulario})




def datos_formulario(request):

    if request.method == "POST":

        formulario = DatosFormulario(request.POST)

        #print("formulario")
        #print(formulario)

        print(f" is valid: {formulario.is_valid}")
        if formulario.is_valid():

            datos = formulario.cleaned_data

            telefono = datos.get("telefono")
            email = datos.get("email")
            direccion = datos.get("direccion")

            datos = DatosDeContacto(telefono=telefono, email=email, direccion=direccion)

            datos.save()

            return render(request, 'index.html') 
        
    else:
        formulario = DatosFormulario()


    return render(request, 'datos_formulario.html', {"formulario": formulario})




def intereses_formulario(request):

    if request.method == "POST":

        formulario = InteresesFormulario(request.POST)

        #print("formulario")
        #print(formulario)

        print(f" is valid: {formulario.is_valid}")
        if formulario.is_valid():

            datos = formulario.cleaned_data

            autos = datos.get("autos")
            animales = datos.get("animales")
            medioambiente = datos.get("medioambiente")
            viajes = datos.get("viajes")

            datos = Intereses(autos=autos, animales=animales, medioambiente=medioambiente, viajes=viajes)

            datos.save()

            return render(request, 'index.html') 
        
    else:
        formulario = InteresesFormulario()


    return render(request, 'intereses_formulario.html', {"formulario": formulario})




def busqueda_dni(request):

    if request.method == "GET":

        dni = request.GET.get("dni")
        print(f"Vamos a buscar el dni: {dni}")



    return render(request, 'busqueda_dni.html')


def buscar_dni(request):

    if request.method == "GET":

        dni = request.GET.get("dni")

        if dni is None:
            return HttpResponse("Enviar el dni a buscar")
        
        #siguiente paso buscar los datos

        persona = Persona.objects.filter(dni__icontains=dni)

        contexto  = {
            "persona": persona,
            "dni": dni
        }

        return render(request, "buscar_dni.html", contexto)





def busqueda_email(request):

    if request.method == "GET":

        email = request.GET.get("email")
        print(f"Vamos a buscar el email: {email}")



    return render(request, 'busqueda_email.html')



def buscar_email(request):

    if request.method == "GET":

        email = request.GET.get("email")

        if email is None:
            return HttpResponse("Enviar el email a buscar")
        
        #siguiente paso buscar los datos

        datos = DatosDeContacto.objects.filter(email__icontains=email)

        contexto  = {
            "datos": datos,
            "email": email
        }

        return render(request, "buscar_email.html", contexto)
    



def busqueda_intereses(request):

    if request.method == "GET":

        id = request.GET.get("id")
        print(f"Vamos a buscar el id: {id}")



    return render(request, 'busqueda_intereses.html')


def buscar_intereses(request):

    if request.method == "GET":

        id = request.GET.get("id")

        if id is None:
            return HttpResponse("Enviar el id a buscar")
        
        #siguiente paso buscar los datos

        intereses = Intereses.objects.filter(id__icontains=id)

        contexto  = {
            "intereses": intereses,
            "id": id
        }

        return render(request, "buscar_intereses.html", contexto)