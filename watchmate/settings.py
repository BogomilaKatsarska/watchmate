"""
1. API:
	- middleman
	- example: Uber and Google Maps
	- Client --> Middleman --> Server
	1.1.Types of API:
		- private (within organization - single backend for web, ios, android, etc.)
		- partner (business, when we organize content for business partner - prime video pays to imdb to show the rating for moveis)
		- public, third party API(example: CoinMarketCap, OpenWeather Map) (when everyone is allowed to access the data)
	- use XML/JSON to send/receive response
2. Understanding URLs:
	- follow a particular URL Structures
	BASE URL + ... (END POINT)
	/movies
	/movies/list
	/movies/127
	/movies/127/reviews
	/movies/127/reviews/?limit=20

	/account/login
	/account/register
2. Understanding REST API:
	- REST = REpresentational State Transfer
	2.1.Endpoint:
		- should follow specific structure:
		https://www.api.movielist.com/movies/list
		https://movielist.com/api/movies/list
	2.2.Method
		CRUD = PUT, GET, PUT, DELETE
	2.3.Headers - status codes
	2.4.The Data/Body - JSON/XMLddd for both sides transfer
3. Serialization and Deserialization:
    - Serialization - converting complex data type(Model Object) to python native data type(python dict)
    is known as serialiation
    - JSON DATA ---parse data---> Python Native Data Type ---deserialize---> complex data type
    3.1.Types of Serializers:
        - serializers.Serializer
        - serializers.ModelSerializer
    3.2.Types of Views:
        - CBV - utilize (APIView)
        - FBV - utilize @api_view
4.Postman: GET request with authentication required:
    Headers -> Tick -> Authorization -> value: Basic user:pass (convert to Base64 format)
5.Token: Authorization -> passed in Headers -> Token:value of token
    - POST request to 127.0.0.1:8000/account/login
    BODY(form data):
    username bogomila
    password 123
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-qrzbni1q&@4r&h()003i0^m*$$6d4-x0-v#9%c!be--g0twyb)'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',

    'watchlist_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'watchmate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'watchmate.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#we add below to request all visitors to be logged in
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ]
# }

#BASIC Authentication - for test purposes
REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.BasicAuthentication',
    #     # 'rest_framework.authentication.SessionAuthentication',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}