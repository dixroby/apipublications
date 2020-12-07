from .views import PublicacionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PublicacionViewSet)

urlpatterns = router.urls