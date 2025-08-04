from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrarRedirect, name='cadastrarRedirect'),
    path('deletar_aluno/<int:id>', views.deletar_aluno, name='deletar_aluno'),
    path('atualizar_aluno/<int:id>', views.atualizar_aluno, name='atualizar_aluno')
]