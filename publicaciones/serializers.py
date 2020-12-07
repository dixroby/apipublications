from rest_framework import serializers
from comentarios.serializers import ComentarioSerializer
from tags.serializers import TagSerializer

from publicaciones.models import Publicacion

class PublicacionSerializer(serializers.ModelSerializer):
    
    comentarios = ComentarioSerializer(read_only=True, many=True)
    tag = TagSerializer(read_only=True, many=True)
    class Meta :
        model = Publicacion
        fields = '__all__'