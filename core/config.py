# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bozcgnf^9^w^9f!l!!pctrfs+ww+882u0pn8j9u1d+!4ql=*jg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
