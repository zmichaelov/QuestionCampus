import os
import sys

sys.path.append("/home/zmichaelov/webapps/duke_exchange/osqa")
sys.path.append("/home/zmichaelov/webapps/duke_exchange/")

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'osqa.settings'
application = WSGIHandler()
