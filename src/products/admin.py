from django.contrib.admin import TabularInline, register
from django.utils.html import format_html

from src.common.admin import BaseAdmin, SaveModelAdmin

from .models import Category, ProductImage, ProductItem


@register(Category)
class CategoryAdmin(BaseAdmin, SaveModelAdmin):  # type: ignore
    """
    Admin configuration for Category Model
    """

    fieldsets = (
        (
            None,
            {"fields": ("name", "description", "icon")},
        ),
    )
    list_display = ["name", "created_by", "updated_by", "created", "modified"]
    list_filter = ["created", "modified"]
    search_fields = ["name"]


class ProductImageInline(TabularInline):  # type: ignore
    """
    Inline configuration for ProductImage in the admin interface.
    """

    model = ProductImage
    exclude = ["updated_by"]
    view_on_site = False
    readonly_fields = ("image_preview",)

    def image_preview(self, obj) -> str:  # type: ignore
        """
        Custom method to display product item image preview in the Django admin.

        Returns:
            str: An HTML string containing an image tag displaying the image preview,
            or a string indicating the absence of an image if 'obj.images' is empty.
        """
        if obj.image:
            return format_html(
                f"<img src='{obj.image.url}' style='object-fit:contain; max-width:200px; max-height:200px' />"
            )
        else:
            return "(No image)"

    image_preview.short_description = "Preview"  # type: ignore[attr-defined]


@register(ProductItem)
class ProductItemAdmin(BaseAdmin, SaveModelAdmin):  # type: ignore
    """
    Admin configuration for ProductItem Model
    """

    inlines = [ProductImageInline]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "category",
                    "description",
                    "stock",
                    "og_price",
                    "price",
                    "is_published",
                    "is_new_arrival",
                    "is_featured",
                ),
            },
        ),
    )
    list_display = [
        "name",
        "category",
        "created_by",
        "updated_by",
        "created",
        "modified",
    ]
    list_filter = ["created", "modified"]
    search_fields = ["name"]
