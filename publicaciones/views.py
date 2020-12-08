from django.shortcuts import render
from publicaciones.serializers import PublicacionSerializer
from comentarios.serializers import ComentarioSerializer
from tags.serializers import TagSerializer

from comentarios.models import  Comentario
from publicaciones.models import  Publicacion
from tags.models import Tag

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
# Create your views here
# .
class PublicacionViewSet(viewsets.ModelViewSet):

   queryset = Publicacion.objects.all()
   serializer_class = PublicacionSerializer
   permission_classes = (AllowAny, )

   @action(methods=['GET', 'POST', 'DELETE'], detail=True)
   def tags(self, request, pk=None):
      publicacion = self.get_object()

      if request.method == 'GET':
         serializer = TagSerializer(publicacion.tag, many=True)
         return Response(status=status.HTTP_200_OK, data=serializer.data)

      if request.method == 'POST':
         tag_id = request.data['tags_ids']
         for id_tag in tag_id:
            try:
               tag = Tag.objects.get(id=id_tag)
               publicacion.tag.add(tag)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"messaje":"Tag does not exist"})

         serializer = TagSerializer(publicacion.tag, many=True)
         return Response(status=status.HTTP_201_CREATED, data=serializer.data)

      if request.method == 'DELETE':
         comet_id = request.data['tags_ids']

         for id_com in comet_id:
            comentario = Tag.objects.get(id=id_com)
            publicacion.tag.remove(comentario)

         serializer = TagSerializer(publicacion.tag, many=True)
         return Response(status=status.HTTP_200_OK, data=serializer.data)

   @action(methods=['GET'], detail=True)
   def comentarios(self, request, pk=None):
      publicacion = self.get_object()
      print("hola")
      print(publicacion)
      if request.method == 'GET':
         serializer = ComentarioSerializer(publicacion.comentarios,many=True)
         return Response(status=status.HTTP_200_OK, data=serializer.data)