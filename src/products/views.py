from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import ProductItem
from .serializers import ProductItemSerializer


class ProductReadOnlyViewSet(ReadOnlyModelViewSet):  # type: ignore
    queryset = ProductItem.objects.published()
    serializer_class = ProductItemSerializer
    lookup_field = "slug"
