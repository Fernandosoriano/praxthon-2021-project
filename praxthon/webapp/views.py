from django.shortcuts import render
from personas.models import Persona
from django.db.models import  Q 


def bienvenido(request):
    # print(request.GET)
    habilidad_query_set  = request.GET.get("Habilidad")
    perfil_query_set  = request.GET.get("Perfil")
    print(habilidad_query_set,perfil_query_set)
    if habilidad_query_set or perfil_query_set:
        filtrados = True
        res_filtrados = Persona.objects.filter(
            Q(perfil = perfil_query_set ) |
            Q(habilidades = habilidad_query_set)
            
        )
        return render (request,'filtrados.html',{'filtrados': filtrados, 'res_filtrados':res_filtrados})
    

    # cada clase de modelo tiene acceso a un atributo llamado objects, manejador, que te permite  traer información de la BD
    no_personas = Persona.objects.count() # con count obtienes el número de personas desde la BD
    return render (request,'inicio.html',{'no_personas':no_personas})