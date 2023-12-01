from django.contrib.admin import TabularInline, register

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
