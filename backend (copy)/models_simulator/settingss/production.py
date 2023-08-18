from .common import *
###############
## configuration for heroku
# import dj_database_url
# import django_heroku
####################

DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1','localhost','localhost:8282','devarchive.org','www.devarchive.org','devarchive.org:8181','www.devarchive.org:8181']
ALLOWED_HOSTS = ['*']


CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8181',
    'http://devarchive.org',
    'https://devarchive.org',
    'http://www.devarchive.org',
    'https://www.devarchive.org',
    'http://devarchive.org:8181',
    'http://www.devarchive.org:8181',
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8181',
    'http://devarchive.org',
    'https://devarchive.org',
    'http://www.devarchive.org',
    'https://www.devarchive.org',
    'http://devarchive.org:8181',
    'http://www.devarchive.org:8181',
]


# TEST/DEVELOPMENT REMOTE DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     # 'default': {},
#     'default': {
#         'ENGINE': os.environ.get('MYSQL_ENGINE'),
#         'NAME': os.environ.get('MYSQL_DATABASE'),
#         'USER': os.environ.get('MYSQL_USER'),
#         'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
#         'HOST': os.environ.get('MYSQL_HOST'),
#         'PORT': os.environ.get('MYSQL_PORT'),
#         'OPTIONS': {
#             'auth_plugin': 'mysql_native_password'
#         }

#     },
# }

