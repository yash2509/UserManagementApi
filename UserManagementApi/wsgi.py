"""
WSGI config for UserManagementApi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UserManagementApi.settings')
#WEB SERVER GATEWAY INTERFACE(FOR HTTP HANDLING)
application = get_wsgi_application()
