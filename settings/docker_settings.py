from .base_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'docker',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': 'db',
        'PORT': 5432,
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LEAFLET_CONFIG = {
    # 'DEFAULT_CENTER': (52.525649, 13.480383),
    # 'DEFAULT_ZOOM': 13,
    'ATTRIBUTION_PREFIX': '',
}
