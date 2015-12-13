"""
WSGI config for blackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en//howto/deployment/wsgi/
"""
from dj_static import Cling, MediaCling
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blackend.settings")

application = Cling(MediaCling(get_wsgi_application()))