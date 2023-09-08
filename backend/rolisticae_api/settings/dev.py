from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-omp7^&au2mzcu7qn@x3%6aa#jx)eozapxsbj_q_*@yxfx^vqz2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
print("Using dev settings")
print("BASE_DIR is:", BASE_DIR)
print("DATABASES is:", DATABASES)   

# Other settings specific to the development environment
