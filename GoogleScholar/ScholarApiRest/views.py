#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ScholarApiRest.models import *
from ScholarApiRest.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
import json

class AutoresList(APIView):
    """
    Obtener lista de Autores
    """
    def get(self, request, format=None):
        snippets = []
        autores = AutorPublicacion.objects.values('cedula').distinct()

        for autor in autores:
            filtro = AutorPublicacion.objects.filter(cedula=autor['cedula'])
            snippets.append(filtro[0])

        serializer = AutorPublicacionSerializer(snippets, many=True)
        return Response(serializer.data)

class AutoresInfo(APIView):
    """
    Obtener Autor
    """
    def get(self, request, pk, format=None):
        snippets = AutorPublicacion.objects.values('id', 'cedula', 'tipo_docente',\
         'apellido', 'nombre', 'scholar_url', 'email').filter(cedula=pk)[:1]
        print snippets
        serializer = AutorPublicacionSerializer(snippets, many=True)
        return Response(serializer.data)

class AutoresDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return PerfilGoogle.objects.filter(cedula=pk)
        except PerfilGoogle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PerfilGoogleSerializer(snippet, many=True)
        return Response(serializer.data)

class ValidarPerfil(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return PerfilGoogle.objects.get(id=pk)
        except PerfilGoogle.DoesNotExist:
            raise Http404
    def get_usuario(self, pk):
        try:
            return AutorPublicacion.objects.filter(cedula=pk)
        except AutorPublicacion.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PerfilGoogleSerializer(snippet, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''class UsuarioDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Usuario.objects.get(nick=pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        print snippet
        serializer = UsuariosSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UsuariosSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProgramasUsuario(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, pk, format=None):
        snippets = Programas.objects.filter(id_usuario=pk)
        print snippets
        serializer = ProgramasSerializer(snippets, many=True)
        return Response(serializer.data)


class ProgramasList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Programas.objects.all()
        print snippets
        serializer = ProgramasSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print request.data
        print os.getcwd()        
        nombre = request.data['nombre']+'.py'
        fichero = open(nombre, 'w')
        fichero.write(request.data['codigo'])
        fichero.close()
        resultado = commands.getoutput("python "+nombre)
        request.data['resultado'] = resultado
        print request.data
        serializer = ProgramasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''


