from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar  # Asegúrate de que el modelo Familiar esté definido en models.py

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

def crear_familiar(request, nombre):
   if nombre is not None:
        nuevo_familiar = Familiar(
            nombre=nombre,
            apellido='serratto',
            edad=26, 
            fecha_nacimiento='1997-02-06',  
            parentesco="hermano"

            )

        nuevo_familiar.save()
        return render(request, 'mi_primer_app/crear_familiar.html', {"nombre": nombre})
