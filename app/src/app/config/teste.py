from .base import *

BASIC_AUTH_PASSWORD = 'A3uUWjC2759429'

JWT_SECRET_KEY = f"{SECRET_KEY}.6oanDb619zfM32hrbhpdrUt"

DATABASE =  {
    'ENGINE': 'sqlite',
    'NAME': ':memory:'
}

DEBUG = False