from django.db import models
from publicaciones.models import Publicacion


class Comentario(models.Model):
    
    comentario = models.CharField(max_length=200)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE,related_name='comentarios') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comentario