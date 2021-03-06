from urllib import request

from django.shortcuts import render

from tags.models import  Tag
from publicaciones.models import Publicacion

from tags.serializers import TagSerializer
from comentarios.serializers import ComentarioSerializer
from publicaciones.serializers import  PublicacionSerializer

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
# Create your views here
# .
class TagViewSet(viewsets.ModelViewSet):
   queryset = Tag.objects.all()
   serializer_class = TagSerializer
   permission_classes = (AllowAny, )


   @action(methods=['GET', 'POST', 'DELETE'], detail=True)
   def publicaciones(self, request, pk=None):
      comentarios = self.get_object()
      if request.method == 'GET':
         serialized = PublicacionSerializer(comentarios.publicaciones, many=True)
         return Response(status=status.HTTP_200_OK, data=serialized.data)

      if request.method == 'POST':
         public_id = request.data['publicaciones_ids']

         for id_com in public_id:
            try:
               publicacion = Publicacion.objects.get(id=id_com)
               comentarios.publicaciones.add(publicacion)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"messaje":"Post does not exist"})

         serializer = PublicacionSerializer(comentarios.publicaciones, many=True)
         return Response(status=status.HTTP_201_CREATED, data=serializer.data)

      if request.method == 'DELETE':

          public_id = request.data['publicaciones_ids']

          for id_com in public_id:
              try:
                  publicacion = Publicacion.objects.get(id=id_com)
                  comentarios.publicaciones.remove(publicacion)
              except:
                  return Response(status=status.HTTP_404_NOT_FOUND, data={"messaje":"Post does not exist"})

          serializer = PublicacionSerializer(comentarios.publicaciones, many=True)
          return Response(status=status.HTTP_201_CREATED, data=serializer.data)