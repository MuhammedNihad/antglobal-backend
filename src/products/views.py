from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import ProductItem
from .serializers import ProductItemListSerializer, ProductItemSerializer


class ProductReadOnlyViewSet(ReadOnlyModelViewSet):  # type: ignore
    queryset = ProductItem.objects.published()
    serializer_class = ProductItemSerializer
    lookup_field = "slug"

    def get_serializer_class(
        self,
    ) -> ModelSerializer:
        """
        Determine the appropriate serializer class based on the view's action.

        If the action is 'list', return the ProductItemListSerializer class, which includes a field named 'images' that
        can be set as thumbnails and is fetched using the get_first_image() model manager method.
        Otherwise, return ProductItemSerializer which includes all images of product.
        """
        if self.action == "list":
            return ProductItemListSerializer
        return ProductItemSerializer
