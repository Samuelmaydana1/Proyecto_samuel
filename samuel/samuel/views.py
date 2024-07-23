from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola mundo!, hola Samuel!")

def dia_de_hoy(request):
    dia = datetime.now()
    return HttpResponse(f"Hoy es día:<br>{dia}")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido!")

def probando_template(request):

    nombre = "Adrian"
    apellido = "Holovaty"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
    }

    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)