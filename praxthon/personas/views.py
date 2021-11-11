from django.shortcuts import redirect, render
from django.forms import modelform_factory
from personas.models import Persona

# Create your views here.

PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST': #valida si cliente esta enviando info 
        formaPersona = PersonaForm(request.POST) #obtienes info que envia el cliente desde el formulario
        if formaPersona.is_valid(): #validas
            formaPersona.save() #se hace insert a la bd
            return redirect('index')
    else:   # en este caso es un get, es decir cuando le doy click a agregar persona
        formaPersona  = PersonaForm()  # llenas form en blanco  con la clase de modelo de Persona
    
    return render(request,'personas/nuevo.html',{'formaPersona':formaPersona})

def traerPersonas(request):
    personas = Persona.objects.all() #manejador obejects , all me trae toda la info 
    return render (request,'personas/registradas.html',{'personas': personas})


