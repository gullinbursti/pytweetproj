# Django settings for pytweetproj project.
import os
APPLICATION_DIR = os.path.dirname( globals()[ '__file__' ] )

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

# we'll use sqlite3 for caching
DATABASE_ENGINE = 'sqlite3'           
DATABASE_NAME = 'session.db'             
DATABASE_USER = ''             
DATABASE_PASSWORD = ''         
DATABASE_HOST = ''             
DATABASE_PORT = ''             

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# if you won't be using internationalization, better to keep
# it false for speed
USE_I18N = False

MEDIA_ROOT = os.path.join( APPLICATION_DIR, 'resources' )
MEDIA_URL = 'http://localhost:8000/resources/'
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=y^moj$+yfgwy2kc7^oexnl-f6(b#rkvvhq6c-ckks9_c#$35'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.contrib.auth.middleware.AuthenticationMiddleware',
) 

ROOT_URLCONF = 'pytweetproj.urls'

TEMPLATE_DIRS = (
     os.path.join( APPLICATION_DIR, 'templates' ), 
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'twitterPanel',
)

# added for sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'