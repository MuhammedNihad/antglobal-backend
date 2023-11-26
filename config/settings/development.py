"""
Settings for development environment
"""

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "SECRET_KEY",
    default="f6SPbr062kxthtgEUOGC8Z4VAat7sJ63K7TIGim6ASR6RA8JfVK53Ti786s2EFo8",
)

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Parse database connection url strings
# like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    #
    # The db() method is an alias for db_url().
    "default": env.db(default="psql://user:pass@127.0.0.1:8458/db"),
    # read os.environ['SQLITE_URL']
    "extra": env.db_url(
        "SQLITE_URL", default="sqlite:////tmp/my-tmp-sqlite.db"
    ),
}
