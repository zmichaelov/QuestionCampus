# encoding:utf-8
import os.path

SITE_SRC_ROOT = os.path.dirname(__file__)
LOG_FILENAME = 'django.osqa.log'

#for logging
import logging
logging.basicConfig(
    filename=os.path.join(SITE_SRC_ROOT, 'log', LOG_FILENAME),
    level=logging.ERROR,
    format='%(pathname)s TIME: %(asctime)s MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s',
)

#ADMINS and MANAGERS
ADMINS = ()
MANAGERS = ADMINS

DEBUG = False
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': True
}
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)


DATABASE_NAME = "zmichaelov_duke_exchange"
DATABASE_USER = "zmichaelov_duke_exchange"
DATABASE_PASSWORD = "3dkrv0i3"
DATABASE_ENGINE = "django.db.backends.postgresql_psycopg2"
DATABASE_HOST = ''
DATABASE_PORT = ''

CACHE_BACKEND = 'file://%s' % os.path.join(os.path.dirname(__file__),'cache').replace('\\','/')
#CACHE_BACKEND = 'dummy://'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# This should be equal to your domain name, plus the web application context.
# This shouldn't be followed by a trailing slash.
# I.e., http://www.yoursite.com or http://www.hostedsite.com/yourhostapp
APP_URL = 'http://dukexchange.com'

#LOCALIZATIONS
TIME_ZONE = 'America/New_York'

#OTHER SETTINGS

USE_I18N = True
LANGUAGE_CODE = 'en'

DJANGO_VERSION = 1.1
OSQA_DEFAULT_SKIN = 'duke'

DISABLED_MODULES = ['books', 'recaptcha', 'project_badges','openidauth','facebookauth','oauthauth']
#Email Configuration Settings
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'duke_exchange'
EMAIL_HOST_PASSWORD = 'You c@nt tak3 the $ky from me'
DEFAULT_FROM_EMAIL = 'support@dukexchange.com'
SERVER_EMAIL = 'support@dukexchange.com'
