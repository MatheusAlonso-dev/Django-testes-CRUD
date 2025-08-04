from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno

# Create your views here.
def cadastrarRedirect(request):
    if request.method == 'GET':
        alunos = Aluno.objects.all()
        print(alunos)
        return render(request, 'cadastrar.html',{'alunos':alunos})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        aluno = Aluno(
            nome = nome,
            email = email
        )

        aluno.save()
        return redirect('cadastrarRedirect')

def deletar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('cadastrarRedirect')

def atualizar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    nome = request.POST.get('nome')
    email = request.POST.get('email')

    aluno.nome = nome
    aluno.email = email

    aluno.save()

    return redirect('cadastrarRedirect')