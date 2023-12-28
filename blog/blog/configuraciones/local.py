from .settings import * 
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
LOGIN_REDIRECT_URL = '/'

DATABASES ={
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'datos_base',
        'USER': 'root',
        'PASSWORD': '159357Laio+',
        'HOST': 'LocalHost',
        'PORT': '3306'
    }

}