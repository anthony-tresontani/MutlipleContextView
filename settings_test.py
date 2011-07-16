import os

BASE_DIR = os.path.dirname(__file__)

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'MutlipleContextView.multiplecontexts',
)

TEMPLATE_DIRS = (os.path.join(BASE_DIR,'templates'),)