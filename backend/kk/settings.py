from pathlib import Path
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-vw-*r6!19!*7tg9@k(&h&h4as*!6kietj1jxr-tu)&(vwp*2es'
DEBUG = True
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "rest_framework",         
    "rest_framework.authtoken",
    'rest_framework_simplejwt.token_blacklist',
    "scripts"
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
]
ROOT_URLCONF = 'kk.urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "UNAUTHENTICATED_USER": None,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # Menggunakan JWT untuk semua API yang dilindungi
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # Anda mungkin juga ingin menyertakan SessionAuthentication untuk sesi browser
        'rest_framework.authentication.SessionAuthentication', 
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
AUTH_USER_MODEL = "scripts.User"
CORS_ALLOW_ALL_ORIGINS = True  # untuk dev, production ganti ke whitelist
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080"
]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SIMPLE_JWT = {
    # Access token harus berumur pendek (misalnya, 5 menit)
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5), 
    
    # Refresh token berumur panjang (misalnya, 1 hari)
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    
    # URL untuk mendapatkan token baru (refresh) dari refresh token
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,

    # Mengatur algoritma dan kunci signing
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY, 
    'VERIFYING_KEY': None,
    
    # Header yang digunakan untuk otentikasi (Penting: 'Bearer')
    'AUTH_HEADER_TYPES': ('Bearer',), 
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}