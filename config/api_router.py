from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from src.products.views import ProductReadOnlyViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"products", ProductReadOnlyViewSet, basename="products")

app_name = "api"
urlpatterns = router.urls
