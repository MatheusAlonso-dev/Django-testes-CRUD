from django.shortcuts import render, redirect
from django.http import HttpResponse
from cadastrar import urls

# Create your views here.

def login(request):
    if request.method == "GET":        
        return render(request, 'login.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        print(usuario)
        print(senha)
        return redirect('cadastrarRedirect')
