BASIC_AUTH_USERNAME = 'api.user'
BASIC_AUTH_PASSWORD = '4PXcpBho3Bl439'

SECRET_KEY = "mN9equWcX7YApaI4FksfIUW0uOwCd3"
JWT_SECRET_KEY = f"{SECRET_KEY}.jCe55syCM7bRWm66PHmJN90Gpti7ae"

DATABASE =  {
    'ENGINE': 'mysql+mysqlconnector',
    'NAME': 'b2bit_db',
    'USER': 'b2bit_db_user',
    'PASSWORD': '6y6RnXmYZ49',
    'HOST': 'localhost',
    'PORT': '3306'
}

ALLOWED_ORIGINS = [
    "http://localhost:5173"
]