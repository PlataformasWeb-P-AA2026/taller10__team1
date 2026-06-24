from ordenamiento.models import Parroquia, Barrio, PresidenteBarrio
from django.http import request
from django.shortcuts import render, redirect
from django.db.models import Sum
from ordenamiento.forms import ParroquiaForm, BarrioForm

# Create your views here.

def index(request):
    parroquias = Parroquia.objects.all()
    barrios = Barrio.objects.all()
    presidentes = PresidenteBarrio.objects.all()
    informacion_template = {
        'parroquia': parroquias,
        'numero_parroquias': parroquias.count(),
        'barrio': barrios,
        'numero_barrios': barrios.count(),
        'presidenteBarrio': presidentes,
        'numero_presidentes_barrio': presidentes.count(),
    }

    return render(request, 'index.html', informacion_template)


def listar_parroquias(request):
    parroquias = Parroquia.objects.annotate(
        total_parques=Sum('barrios__numero_parques')
    ).prefetch_related('barrios__presidentes')
    
    return render(request, 'listar_parroquias.html', {'parroquias': parroquias})


def listar_barrios(request):
    barrios = Barrio.objects.select_related('parroquia').all()
    return render(request, 'listar_barrios.html', {'barrios': barrios})


def crear_parroquia(request):
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_parroquias')
    else:
        formulario = ParroquiaForm()
    return render(request, 'crear_parroquia.html', {'formulario': formulario})


def editar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_parroquias')
    else:
        formulario = ParroquiaForm(instance=parroquia)
    return render(request, 'editar_parroquia.html', {'formulario': formulario})


def crear_barrio(request):
    if request.method == 'POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_barrios')
    else:
        formulario = BarrioForm()
    return render(request, 'crear_barrio.html', {'formulario': formulario})


def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method == 'POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_barrios')
    else:
        formulario = BarrioForm(instance=barrio)
    return render(request, 'editar_barrio.html', {'formulario': formulario})