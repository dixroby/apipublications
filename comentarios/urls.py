from .views import ComentarioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ComentarioViewSet)

urlpatterns = router.urls