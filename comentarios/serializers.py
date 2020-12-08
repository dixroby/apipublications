from rest_framework import serializers
from comentarios.models import Comentario
from publicaciones.models import Publicacion

class PublicationSerializer(serializers.ModelSerializer):
    class Meta :
        model = Publicacion
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    publicacion = PublicationSerializer(read_only=True)
    class Meta :
        model = Comentario
        fields = '__all__'