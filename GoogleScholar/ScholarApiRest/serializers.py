from django.forms import widgets
from rest_framework import serializers
from ScholarApiRest.models import *

class AutorPublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorPublicacion
        fields = ('id', 'cedula', 'email', 'tipo_docente', 'apellido', 'nombre', 'tipo_publicacion', 'titulo', 'abstract', 'year', 'doi', 'keywords', 'enlace_articulo', 'tipo_documento', 'estado', 'scholar_url', 'analizado')

class PerfilGoogleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilGoogle
        fields = ('id', 'cedula', 'scholar_id', 'coincidencia', 'estado')
