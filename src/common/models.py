import uuid

from django.db.models import Model, UUIDField
from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel, Model):  # type: ignore
    """
    An abstract base class provides UUID as the primary key and timestamp fields on any model that inherits from it.
    """

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
