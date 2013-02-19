from django.db import models

# Create your models here.

class Pessoa(models.Model):
    primeiroNome = models.CharField(max_length = 50)
    segundoNome = models.CharField(max_length = 50)
    cidade = models.CharField(max_length = 50)
    telefone = models.CharField(max_length = 15)
    idade = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.primeiroNome
    
class NovaPessoa(models.Model):
    NprimeiroNome = models.CharField(max_length = 50)
    NsegundoNome = models.CharField(max_length = 50)
    algumaCoisa = models.CharField(max_length = 50)