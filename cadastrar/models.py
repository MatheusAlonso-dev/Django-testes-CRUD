from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    teste = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nome