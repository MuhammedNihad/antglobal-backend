from django.contrib.admin import ModelAdmin


class BaseAdmin(ModelAdmin):  # type: ignore
    """
    BaseAdmin  admin class that can be inherited by all other admin classes related to models to provide common functionality.

    Attributes:
        view_on_site (bool): Indicates whether the "View on site" link should be displayed. Set to False.

        show_full_result_count (bool): Indicates whether the full result count should be displayed
                                      in the admin change list header. Setting this to True
                                      generates a query to perform a full count on the table,
                                      which can be expensive if the table contains a large number
                                      of rows. Set to False to avoid performance impact.
    """

    view_on_site = False
    show_full_result_count = False


class SaveModelAdmin(ModelAdmin):  # type: ignore
    """
    SaveModelAdmin is a custom ModelAdmin extension designed for saving models with additional user tracking.
    This class overrides the default save_model method to automatically populate the created_by and updated_by fields
    with the current user when creating or updating an object through the Django admin interface.
    """

    def save_model(self, request, obj, form, change):  # type: ignore
        if not change:
            # If the model is being created, set the created_by field to the current user.
            obj.created_by = request.user

        # Regardless of creation or modification, update the updated_by field to the current user.
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
