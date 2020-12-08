from rest_framework import serializers
from tags.models import Tag
#from publicaciones.serializers import PublicacionSerializer
from publicaciones.models import Publicacion

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'
class TagSerializer(serializers.ModelSerializer):
    publicaciones = PublicacionSerializer(read_only=True, many=True)
    #publicaciones = Publicaciones
    class Meta :
        model = Tag
        fields = '__all__'