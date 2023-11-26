from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommonConfig(AppConfig):  # type: ignore
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.common"
    verbose_name = _("Common")