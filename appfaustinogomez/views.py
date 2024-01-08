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


"""
def persona_formulario(request):

    print(f"path: {request.path}")
    print(f"full path: {request.get_full_path()}")
    print(f"host: {request.get_host()}")
    print(f"si es segura: {request.is_secure()}")
    print(f"metodo: {request.method}")
    ua = request.META.get("HTTP_USER_AGENT")
    print(f"ua: {ua}")

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        dni = request.POST.get("dni")

        print(f" el nombre es {nombre}, el apellido es {apellido} y su dni es {dni}")


        persona = Persona(nombre=nombre, apellido=apellido, dni=dni)

        persona.save()

        return render(request, 'index.html')

    return render(request, 'persona_formulario.html')

"""
def persona_formulario(request):

    if request.method == "POST":

        formulario = PersonaFormulario(request.POST)

        #print("formulario")
        #print(formulario)

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