from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


def natal(request):
    return HttpResponse('<h1>Oi mundo<h1>')

# def natal(request):
 # return render(request, 'natal.html')"

hoje = date.today()

def verificadata():
    if(hoje.day == 25 and hoje.month == 12):
        contexto = {'natal': True,
        'carnaval': False}

    if(hoje.day == 20 and hoje.month == 4):
        contexto = {'natal': False,
        'carnaval': True}

    if(hoje.day == 13 and hoje.month == 4):
        contexto = {'tiradentes': True}

    return contexto

def natal(request):
    verificadata()
    return render(request, 'natal.html', verificadata())

def tiradentes(request):
    verificadata()
    return render(request, 'tiradentes.html', verificadata())