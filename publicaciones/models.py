from django.db import models
from tags.models import Tag
import uuid

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Publicacion(TimeStampMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.CharField(max_length=200)
    publicacion = models.CharField(max_length=200)

    tag = models.ManyToManyField(Tag, related_name='publicaciones')
    
    def __str__(self):
        return self.publicacion