from datetime import date
from django.db import models
from django.db.models.query import QuerySet
from django.http import request
from django.shortcuts import render,redirect,get_object_or_404
from django.http.response import HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import Producto,Categoria
from .forms import ProductForm,RegistroForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import SESSION_KEY, authenticate,login
from django.contrib import messages
from django.db.models import Q



## necesitamos tener las tareas en sesiones
#tareas = ["bañarse", "vestirse", "prepararcosas", "salir", "tomar colectivo"]

class FormAltaTarea(forms.Form):
    tarea=forms.CharField(label="Nueva Tarea")





def agregar(request):
    if request.method=="POST":
        form=FormAltaTarea(request.POST)
        if form.is_valid():
            tarea=form.cleaned_data["tarea"]
            request.session["tareas"] += [tarea]
            return HttpResponseRedirect(reverse("Final:index"))
        else:
            return render(request,"hola/nProducto.html")
    else:
        return render(request,"hola/nProducto.html")


def agregar_producto(request):
    data={
        'form':ProductForm()
    }
    
    if request.method =='POST':
        print(request.POST)
        formulario=ProductForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            print("paso el segundo")
            formulario.save()
            messages.success(request,"Agregado Correctamente")
            return HttpResponseRedirect(reverse("Final:index"))
        else:
            data['form']=formulario
            print("no funcaaAaa")

    return render(request,'hola/nProducto.html',data)


def modificar_producto(request, id):
    producto=Producto.objects.get(id=id)
    data={
        'form':ProductForm(instance=producto)
    }

    if request.method == 'POST':
        formulario=ProductForm(data=request.POST,instance=producto,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Moficado Correctamente")
            return HttpResponseRedirect(reverse('Final:index'))
        data["form"] = formulario

    return render(request,'hola/modificar_producto.html',data)

def eliminar_producto(request, id):
    producto=get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request, "eliminado Correctamente")
    return HttpResponseRedirect(reverse('Final:index'))


def listar_productos(request):
    productos=Producto.objects.all().order_by('-id')[:3]
    lista=Producto.objects.all().order_by('-id')[3:10]
    cat=Categoria.objects.all()
    
    data ={
        'productos':productos,
        'lista':lista,
        'cat':cat
    }

    return render(request,'hola/index.html',data)

def busqueda(request):
    queryset=request.GET.get("Buscar")
    print(queryset)
    busqueda=Producto.objects.all()
    
    if queryset:
        busqueda=Producto.objects.filter(
            Q(Nombre__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()
    
    data = {
        'busqueda':busqueda
    }
    
    return render(request,'hola/busquedaR.html',data)
    


def verP(request, id):
    producto=Producto.objects.filter(id=id)

    data ={
        'productos':producto
    }

    if request.method == 'POST':
        formulario=ProductForm(data=request.POST,instance=producto,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
        data["productos"] = formulario


    return render(request,'hola/ver_producto.html',data)

def AcercaDe(request):
    return render(request,'hola/AcercaDe.html')

def registro(request):

    data ={
        'form':RegistroForm()
    }

    if request.method == 'POST':
        formulario=RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data['password1'])
            login(request,user)
            messages.success(request,"te has registrado correctamente")
            return HttpResponseRedirect(reverse('Final:index'))
        data['form']=formulario
    return render(request,'registration/registro.html',data)



# Create your views here.
def index(request):
    if "carro" not in request.session:
        request.session["carro"]=[]
    return render(request,"hola/carro.html",{
        "carro": request.session["carro"]
    })

def carro(request):
    carro=Producto.objects.all()

    data={
        'carro':carro
    }

    if request.method == 'POST':
        formulario=ProductForm(data=request.POST,instance=carro)
        if formulario.is_valid():
            carro = formulario.cleaned_data["carro"]
            request.session["carro"] += [carro]
            return HttpResponseRedirect("Final:Carro")
        data['carro']=formulario
    return render(request,"hola/carro.html",data)




