from rest_framework import serializers
from tags.models import Tag
from comentarios.serializers import ComentarioSerializer
from django.db import models

from publicaciones.models import Publicacion
from comentarios.models import Comentario

class TagSerializer(serializers.ModelSerializer):
    class Meta :
        model = Tag
        fields = '__all__'
class PublicacionSerializer(serializers.ModelSerializer):

    comentarios = ComentarioSerializer(read_only=True, many=True)
    tag = TagSerializer(read_only=True, many=True)
    class Meta :
        model = Publicacion
        #fields = '__all__'
        fields = ('id','publicacion','usuario','created_at','updated_at','tag','comentarios',)