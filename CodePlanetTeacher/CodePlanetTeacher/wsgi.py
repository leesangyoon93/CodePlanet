"""
WSGI config for CodePlanetTeacher project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import os

from django.core.wsgi import get_wsgi_application

env = os.environ.get('CODEPLANET_ENV')

if env:
    if not env.endswith('_settings'):
        env = '{}_settings'.format(env)
else:
    env = 'settings'

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "CodePlanetTeacher.{}".format(env)
)

application = get_wsgi_application()
