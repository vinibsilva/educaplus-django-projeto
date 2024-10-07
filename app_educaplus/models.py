from django.db import models

class Estudante(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=150)
    email = models.TextField(max_length = 150)
    data_nascimento = models.DateField()
    senha = models.TextField(max_length=50)