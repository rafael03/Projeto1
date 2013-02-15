from django.db import models
import datetime
from django.utils import timezone


# Create your models here

class NovoUsuario(models.Model):
    Usuario_nome = models.CharField(max_length=200)
    Hora_cadastro = models.DateTimeField('Hora do Cadastro')

    def __unicode__(self):
        return self.Usuario_nome

