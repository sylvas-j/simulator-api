"""
WSGI config for models_simulator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'models_simulator.settings')

# application = get_wsgi_application()


import os
from django.core.wsgi import get_wsgi_application
from helpers.credentials import dev_prod

dev_prod()

application = get_wsgi_application()

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'srms_project.settings')

# configuration for heroku
######################
from whitenoise import WhiteNoise
# from whitenoise.django import DjangoWhiteNoise
application = WhiteNoise(application)
#######################

