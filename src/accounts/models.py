import uuid

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, UUIDField
from django.utils.translation import gettext_lazy as _

from src.accounts.managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Default custom user model.
    """

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail/change page view in the admin site.

        Returns:
            str: URL for user detail/change page view in the admin site..

        """
        return f"/admin/accounts/customuser/{self.id}"
