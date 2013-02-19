from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, include, url


urlpatterns = patterns('TesteModels.views',
    url(r'^$',         'index'),
    url(r'exibir/$',                        'mostrar'),
    url(r'^(?P<pessoa_id>\d+)/alterar/$',   'alterar'),
    url(r'cadastrar/$',         'cadastrar'),

              
)
#    url(r'^(?P<poll_id>\d+)/vote/$',        'vote'),
