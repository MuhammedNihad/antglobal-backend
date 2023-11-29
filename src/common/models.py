import uuid

from django.conf import settings
from django.db.models import SET_NULL, ForeignKey, Model, UUIDField
from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel, Model):  # type: ignore
    """
    An abstract base class provides UUID as the primary key,
    created_by and updated_by fields referencing user model,
    and timestamp fields to any model that inherits from it.
    """

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_by = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=SET_NULL,
        null=True,
        editable=False,
        related_name="%(class)s_created_by",
    )
    updated_by = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=SET_NULL,
        null=True,
        related_name="%(class)s_updated_by",
    )

    class Meta:
        abstract = True
