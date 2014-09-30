"""
    Django settings for mymtero project.
    
    For more information on this file, see
    https://docs.djangoproject.com/en/1.6/topics/settings/
    
    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/1.6/ref/settings/
    """

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'irp%x1j)a8cu1xmol&0jc82^)r))f#9s&7eu=x-v$gzsuoj!jx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
                  'django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'metro',
                  'django.contrib.admin',
                  'django.contrib.admindocs',
                  
                  
                  
                  
                  )

MIDDLEWARE_CLASSES = (
                      'django.contrib.sessions.middleware.SessionMiddleware',
                      'django.middleware.common.CommonMiddleware',
                      'django.middleware.csrf.CsrfViewMiddleware',
                      'django.contrib.auth.middleware.AuthenticationMiddleware',
                      'django.contrib.messages.middleware.MessageMiddleware',
                      'django.middleware.clickjacking.XFrameOptionsMiddleware',
                      )

ROOT_URLCONF = 'mymtero.urls'

TEMPLATE_DIRS = {
    
    "metro/templates",

}

WSGI_APPLICATION = 'mymtero.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'metrod',
        'USER': 'root',
        'PASSWORD': 'adityagupta',
        'HOST': '',
        'PORT': '',
        
        
        
        }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = ''

STATIC_URL = '/static/'


STATICFILES_DIRS = (
                    
                    "metro/static",
                    
                    
                    )


STATICFILES_FINDERS = (
                       
                       'django.contrib.staticfiles.finders.FileSystemFinder',
                       'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                       
                       
                       )


TEMPLATE_CONTEXT_PROCESSORS = (
                               "django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               )




