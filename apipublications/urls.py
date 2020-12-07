from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comentarios/', include('comentarios.urls')),
    path('publicaciones/', include('publicaciones.urls')),
    path('tags/', include('tags.urls')),
]