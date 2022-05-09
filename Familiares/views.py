from django.shortcuts import render
from .models import Familiares, redirect

def mostrar_Familiares(request):
    familia= Familiares.objects.all()
    context= {'familia':Familiares}
    return render(request,'index.html',context)

def crear_Familiar(request):
    nombre = request.POST["nombre"]
    edad = request.POST["edad"]
    nacimiento = request.POST["nacimiento"]
    familiar= Familiares(nombre= nombre,edad= edad,nacimiento= nacimiento)
    familiar.save()
    return redirect('/familiar/')

def borrar_Familiar(request, id):
    familiar= Familiares.objects.get(id=id)
    familiar.delete()
    return redirect('/familiar/')
