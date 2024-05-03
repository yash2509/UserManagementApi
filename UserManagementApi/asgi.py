"""
ASGI config for UserManagementApi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UserManagementApi.settings')
# Asynchronous Server Gateway Interface
# Designed to support asynchronous, non-blocking I/O, and real-time communication in Python web applications.
application = get_asgi_application()
