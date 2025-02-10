from pathlib import Path

# Definir BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta (¡mantenla segura y no la compartas!)
SECRET_KEY = 'django-insecure-!@#tu_clave_secreta_aqui_1234567890abcdefghijklmnopqrstuvwxyz'

# Configuración de seguridad (DEBUG y ALLOWED_HOSTS)
DEBUG = True  # Cambia a False en producción
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Agrega tu dominio en producción

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',  # Tu aplicación principal
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de URLs
ROOT_URLCONF = 'SpiderVerse.urls'

# Plantillas (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Carpeta global de plantillas
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Base de datos (SQLite por defecto)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Ruta a la base de datos SQLite
    }
}

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "main/static"]  # Ruta a tus archivos estáticos

# Redirecciones de autenticación
LOGIN_URL = 'login'  # Redirige al formulario de inicio de sesión cuando se requiere autenticación
LOGIN_REDIRECT_URL = 'home'  # Redirige al inicio después de iniciar sesión
LOGOUT_REDIRECT_URL = 'home'  # Redirige al inicio después de cerrar sesión

# Configuración de zona horaria e idioma
LANGUAGE_CODE = 'es-mx'  # Cambia a tu idioma preferido
TIME_ZONE = 'America/Mexico_City'  # Cambia a tu zona horaria
USE_I18N = True
USE_TZ = True