from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from ScholarApiRest import views

# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = [
    url(r'^autores/$', views.AutoresList.as_view()),
    url(r'^autores/info/(?P<pk>[0-9]+)/$', views.AutoresInfo.as_view()),
    url(r'^autores/(?P<pk>[0-9]+)/$', views.AutoresDetail.as_view()),
    url(r'^autores/perfil/(?P<pk>[0-9]+)/$', views.ValidarPerfil.as_view()),
    # url(r'^usuarios/(?P<pk>[a-zA-Z]+)/$', views.UsuarioDetail.as_view()),
    # url(r'^programas/$', views.ProgramasList.as_view()),
    # url(r'^programas/pylint/$', views.ProgramasLint.as_view()),
    # url(r'^programas/(?P<pk>[a-zA-Z]+)/$', views.ProgramasDetail.as_view()),
    # url(r'^programas/lista/(?P<pk>[0-9]+)/$', views.ProgramasUsuario.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
