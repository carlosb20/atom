from django.shortcuts import render

def home(request):
    lista = {'lista':['carlos','ana']}
    return render(request,'carlos/home.html',lista)

def sobre(request):
    return render(request,'carlos/sobre.html')

def contado(request):
    return render(request,'carlos/contado.html')
