from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

#Para hacer consultas a la base de datos
from .models import AutorDb,LibroDb

# Create your views here. las vistas se crean basadas en funciones y clases
# Vistas API
def getMensaje(request):
    """Esta es la pagina principal vamos a llamar a una plantilla"""
    #return HttpResponse("Hola mundo")#servidor devolviendo un mensaje
    objeto = AutorDb.objects.all().order_by("-id")#ordena de forma descendente
    return render (request,'index.html',{"objeto":objeto})
#consulta a la base de datos    
def autorView(request,id):  
    autor = get_object_or_404(AutorDb,id=id)    
    return render(request,'autor.html',{'objeto':autor})

#Vistas Apis
def AutorAPIjson(request):
    autores = AutorDb.objects.all()#
    autores_serializados = serialize('json',autores)
    return HttpResponse(autores_serializados,content_type='text/json')
def AutorAPIxml(request):
    autores = AutorDb.objects.all()#
    autores_serializados = serialize('xml',autores)
    return HttpResponse(autores_serializados,content_type='text/xml')