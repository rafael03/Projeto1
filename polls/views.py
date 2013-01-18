# Create your views here.
from polls.models import Poll

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from django.http import Http404


from datetime import datetime


#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    t = loader.get_template('polls/index.html')
#    c = Context ({
#        'latest_poll_list': latest_poll_list,
#    })
#    return HttpResponse(t.render(c))


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})


def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p})


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)


def exibir(request, poll_id):
    horario = datetime.now()
    return HttpResponse(horario)

def mostralista(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    output = '<br>'.join([p.question for p in latest_poll_list])
    return HttpResponse(output) 
