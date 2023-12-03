from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DecimalField,
    FileField,
    ForeignKey,
    ImageField,
    Model,
    PositiveIntegerField,
    TextField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

from src.common.models import BaseModel

from .managers import ProductItemQueryset


class Category(BaseModel, Model):  # type: ignore
    """
    Represents a category for grouping and organizing products.

    Attributes:
        name (str): The name of the category.
        description (str): A brief description of the category.
        icon (File): An optional file field for the category's icon thumbnail.
        is_published (bool): Indicates whether the category is published or not.
        slug (str): Automatically generated slug based on the category name.

    Meta:
        verbose_name_plural (str): Plural name for the model in the admin interface.
    """

    name = CharField(
        _("category name"),
        max_length=128,
        unique=True,
        help_text=_("Specify the name of the category."),
    )
    description = TextField(
        _("description of category"),
        default="",
        max_length=255,
        blank=True,
        help_text=_("Provide a brief description of the category."),
    )
    icon = FileField(
        _("category icon for thumbnail"),
        upload_to="uploads/category-icons",
        blank=True,
        help_text=_(
            "Upload an icon representing the category for use as a thumbnail."
        ),
    )
    is_published = BooleanField(
        _("is category published"),
        default=True,
        help_text=_("Indicate whether the category is published or not."),
    )
    slug = AutoSlugField(
        populate_from="name",
        help_text=_(
            "Automatically generated slug based on the category name."
        ),
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.name}"


class ProductItem(BaseModel, Model):  # type: ignore
    """
    Represents a product with various details and associations.

    Attributes:
        category (Category): The category to which the product belongs.
        name (str): The name of the product.
        description (str): A detailed description of the product.
        og_price (Decimal): The original price of the product.
        price (Decimal): The current price of the product.
        stock (int): The quantity available in stock for this product.
        is_published (bool): Indicates whether the product is published or not.
        is_new_arrival (bool): Marks the product as a new arrival.
        is_featured (bool): Marks the product as a featured item.
        slug (str): Automatically generated slug based on the product name.

    Meta:
        verbose_name (str): Singular name for the model in the admin interface.
        verbose_name_plural (str): Plural name for the model in the admin interface.
    """

    # relations
    category = ForeignKey(
        Category,
        on_delete=CASCADE,
        related_name="categorized_productitems",
        help_text=_("Select the category to which this product belongs."),
    )

    # fields
    name = CharField(
        _("name of product"),
        max_length=255,
        help_text=_("Specify the name of the product."),
    )
    description = TextField(
        _("description of product"),
        default="",
        max_length=255,
        blank=True,
        help_text=_("Provide a detailed description of the product."),
    )
    og_price = DecimalField(
        _("original price of product"),
        default=0.00,
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text=_("Specify the original price of the product."),
    )
    price = DecimalField(
        _("price of product"),
        default=0.00,
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text=_("Specify the current price of the product."),
    )
    stock = PositiveIntegerField(
        _("stock quantity"),
        default=1,
        help_text=_(
            "Specify the quantity available in stock for this product."
        ),
    )
    is_published = BooleanField(
        default=True,
        help_text=_("Indicate whether the product is published or not."),
    )
    is_new_arrival = BooleanField(
        default=False,
        help_text=_("Mark this product as a new arrival."),
    )
    is_featured = BooleanField(
        default=False,
        help_text=_("Mark this product as a featured item."),
    )
    slug = AutoSlugField(
        populate_from="name",
        help_text=_("Automatically generated slug based on the product name."),
    )

    objects = ProductItemQueryset.as_manager()  # type: ignore

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product Items"

    def __str__(self) -> str:
        return f"{self.name} - {self.category.name}"

    def get_absolute_url(self) -> str:
        return reverse("productitem_detail", kwargs={"slug": self.slug})


class ProductImage(BaseModel, Model):  # type: ignore
    """
    Represents an image associated with a product.

    Attributes:
        product (ProductItem): The product to which the image belongs.
        images (File): The image file for the product.
        alt_text (str): Alternative text for the image to enhance accessibility and SEO.
        display_order (int): Specifies the preferred order for displaying the product image.
    """

    # relations
    product = ForeignKey(
        ProductItem,
        on_delete=CASCADE,
        related_name="images",
        help_text=_("Associate this image with a specific product."),
    )

    # fields
    image = ImageField(
        upload_to="uploads/product-images/",
        help_text=_("Upload the image for the product."),
    )
    alt_text = CharField(
        _("alt text of image"),
        max_length=255,
        default="",
        blank=True,
        help_text=_("Specify the alternative text for the image."),
    )
    display_order = PositiveIntegerField(
        _("image display order"),
        default=1,
        help_text=_(
            "Specifies the preferred order for displaying the product image."
        ),
    )

    class Meta:
        verbose_name = "Product Images"
        verbose_name_plural = "Product Images"
        ordering = ["-display_order"]
        unique_together = ("product", "display_order")

    def __str__(self) -> str:
        return f"Image of {self.product.name}"
