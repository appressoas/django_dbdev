from django_dbdev.backends.sqlite import DBSETTINGS

from .base import *  # noqa


DATABASES = {
    'default': DBSETTINGS
}
