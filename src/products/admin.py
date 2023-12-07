from django.contrib.admin import TabularInline, register
from django.forms import BaseInlineFormSet
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


class ProductImageInlineFormSet(BaseInlineFormSet):  # type: ignore
    """
    Custom formset for managing product images in an inline form.

    Overrides the add_fields method to set an initial display order
    for each form field based on the provided index.

    If the index is not None, it calculates the display order by adding
    1 to the integer representation of the index and sets it as the initial
    value for the 'display_order' field in the form.

    Args:
        form: The form to which fields are added.
        index: The index of the form in the form set.

    Attributes:
        current_display_order (int): The calculated display order for the form.
    """

    def add_fields(self, form, index) -> None:  # type: ignore
        if index is not None:
            self.current_display_order = int(index) + 1
            form.fields["display_order"].initial = self.current_display_order
        super().add_fields(form, index)


class ProductImageInline(TabularInline):  # type: ignore
    """
    Inline configuration for ProductImage in the admin interface.
    """

    model = ProductImage
    formset = ProductImageInlineFormSet
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
