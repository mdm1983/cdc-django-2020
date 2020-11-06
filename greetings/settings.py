# INSTALLED_APPS = {'rest_framework'}
import os

INSTALLED_APPS = [
    #'django.contrib.contenttypes',
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'greetings',
    'rest_framework',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',  <- removing this
    ]
}

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
STATICFILES_DIRS = (
  os.path.join(SITE_ROOT, 'static/'),
)