from urllib.request import Request
from django.http import HttpResponse
from django.template import Template,context
from django.template.loader import get_template
from django.shortcuts import render
def saludo(request):
    #doc_externo=get_template('index.html')
    #documento=doc_externo.render()
    return render(request, "index.html")
def menu(request):
    return render(request,"menu.html")
def horarios(request):
    return render(request,"horarios.html")
def trabajador(request):
    return render(request,"trabajador.html")
def login(request):
    return render(request,"login.html")
def gestor(request):
    return render(request,"gestor.html")
def gestor_menu(request):
    return render(request,"gestor_menu.html")
def gestor_horarios(request):
    return render(request,"gestor_horarios.html")
def gestor_platillo(request):
    return render(request,"gestor_platillo.html")
    

