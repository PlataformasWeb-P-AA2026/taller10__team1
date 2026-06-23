from ordenamiento.models import Parroquia, Barrio, PresidenteBarrio
from django.http import request
from django.shortcuts import render

# Create your views here.

def index(request):
    parroquia = Parroquia.objects.all()
    barrio = Barrio.objects.all()
    presidenteBarrio = PresidenteBarrio.objects.all()
    informacion_template = {
        'parroquia': parroquia, 'numero_parroquias': len(parroquia), 
        'barrio': barrio, 'numero_barrios':len(barrio), 
        'presidenteBarrio': presidenteBarrio, 'numero_presidentes_barrio':len(presidenteBarrio)   }
    return render(request, 'index.html', informacion_template)