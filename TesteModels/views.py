from django.template import Context, loader
from datetime import datetime

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from TesteModels.models import Pessoa




def index(request):
    p = Pessoa()
    p.primeiroNome = "Nova"
    p.segundoNome = "SegundoTeste"
    p.cidade = "Brasilia"
    p.telefone = 10
    p.save()
    
    if (p.telefone > 10):
        mensagem = "Seu Telefone e maior que 10"
    else:
        mensagem = "Menor"
        
    y = {'PrimeiroNome' : p.primeiroNome,
         'SegundoNome' : p.segundoNome,
         'Telefone' : p.telefone,
         'Cidade' : p.cidade,
         'Mensagem' : mensagem}
    return render_to_response('TesteModels/index.html',{'dados': y},
                               context_instance=RequestContext(request))
    
def mostrar(request):
    lista = Pessoa.objects.all().order_by('primeiroNome')
    t = loader.get_template('TesteModels/mostrar.html')
    c = Context({'lista':lista,})
    return HttpResponse(t.render(c))


def alterar(request, pessoa_id):
    alterarDados = Pessoa.objects.get(pk=pessoa_id)
    
    y = {'primeiroNome':alterarDados.primeiroNome,
         'segundoNome':alterarDados.segundoNome,
         'telefone': alterarDados.telefone,
         'cidade': alterarDados.cidade}
    return render_to_response('TesteModels/alterar.html',{'alterarDados':y},
                              context_instance=RequestContext(request))
    

def cadastrar(request):
    return render_to_response('TesteModels/cadastrar.html', context_instance=RequestContext(request))