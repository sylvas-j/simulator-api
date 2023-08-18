from .common import *

DEBUG = True
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ALLOWED_HOSTS = ['127.0.0.1','localhost','197.210.227.52']

ALLOWED_HOSTS = ['*']

# CSRF_TRUSTED_ORIGINS = [
#     'http://localhost:8181',
# ]

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:8181',
# ]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     # 'default': {},
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sqldb2',
#         'USER': 'root',
#         'PASSWORD': '',
#         # 'HOST': '192.168.43.197',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         # 'OPTIONS': {
#         #   'init_command': "set sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'"
#         # },
#     },
# }

#TEST/DEVELOPMENT LOCAL DATABASE
DATABASES = {
    # 'default': {},
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'admin_smart_home_ms',
        'USER': 'sylvas',
        'PASSWORD': 'sylvas',
        # 'HOST': '192.168.88.197',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        # 'OPTIONS': {
        #   'init_command': "set sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'"
        # },
    },
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

