from rest_framework.serializers import ModelSerializer

from .models import ProductImage, ProductItem


class ProductImageSerializer(ModelSerializer):  # type:ignore
    """
    Serializer for ProductImage model, facilitating the serialization of ProductImage instances back
    and forth with JSON.

    Args:
        ModelSerializer (_type_): A base serializer class provided by Django REST Framework for
        serializing Django model instances.
    """

    class Meta:
        model = ProductImage
        fields = ["image", "alt_text", "display_order"]


class ProductItemSerializer(ModelSerializer):  # type:ignore
    """
    Serializer for ProductItem model, managing the serialization of ProductItem instances back and
    forth with JSON.

    Attributes:
        images (ProductImageSerializer): Serializer for associated product images.

    Args:
        ModelSerializer (type): A base serializer class provided by Django REST Framework for
            serializing Django model instances.
    """

    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        """
        Specifies the associated model and fields to include in the serialized output.

        Attributes:
            model (ProductImage): The Django model associated with this serializer.
            fields (list): List of fields to include in the serialized representation.
        """

        model = ProductItem
        fields = ["slug", "name", "description", "images"]


class ProductItemListSerializer(ProductItemSerializer):
    """
    Extends ProductItemSerializer to list product items and include a single image suitable for use
    as a thumbnail.

    Attributes:
        images (ProductImageSerializer): Utilizes the custom manager method 'get_first_image()' to retrieve
        only the image with 'display_order=1' for use as the thumbnail or single image of a product.
    """

    images = ProductImageSerializer(
        many=True, read_only=True, source="images.get_first_image"
    )
