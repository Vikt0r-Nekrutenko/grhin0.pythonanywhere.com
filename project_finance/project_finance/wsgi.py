"""
WSGI config for project_finance project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys
import django

import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

path = '/home/grhin0/grhin0.pythonanywhere.com/project_finance/'

if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_finance.settings')

# application = get_wsgi_application()

django.setup()

application = django.core.handlers.wsgi.WSGIHandler()
