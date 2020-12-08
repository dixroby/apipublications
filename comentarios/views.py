from urllib import request

from django.shortcuts import render

from comentarios.models import Comentario
from publicaciones.models import Publicacion

from comentarios.serializers import ComentarioSerializer
from publicaciones.serializers import  PublicacionSerializer


from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

class ComentarioViewSet(viewsets.ModelViewSet):
   queryset = Comentario.objects.all()
   serializer_class = ComentarioSerializer
   permission_classes = (AllowAny, )

   @action(methods=['GET'], detail=True)
   def publicaciones(self, request, pk=None):
      comentario = self.get_object()
      if request.method == 'GET':
         serialized = PublicacionSerializer(comentario.publicacion)
         return Response(status=status.HTTP_200_OK, data=serialized.data)