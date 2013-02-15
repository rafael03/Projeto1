from django.conf.urls import patterns, include, url

urlpatterns = patterns('usuarios.views',
    url(r'^$',          'index'),
    url(r'dados/$',     'Dados'),
    url(r'imagens/$',   'Imagens'),

)

