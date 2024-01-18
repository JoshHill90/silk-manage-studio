from decouple import config

class SETTINGS_KEYS:

    DJANGO_KEY = config('PM_DJANGO_KEY')
    DEBUG_STATE = config('PM_DEBUG_STATE')
    DB_NAME = config('STDB_NAME')
    DB_USER = config('STDB_USER')
    DB_PASSWORD = config('STDB_PASSWORD')
    DB_HOST = config('STDB_HOST')
    DB_PORT = config('STDB_PORT')
    MYSQL_ATTR_SSL_CA = config('STDB_MYSQL_ATTR_SSL_CA')
    dbstt = config('PM_DEBUG_STATE', bool)
    EMAIL_HOSTING = config('PM_EMAIL_HOSTING')
    EMAIL_USER = config('PM_EMAIL_USER')
    EMAIL_PASSWORD = config('PM_EMAIL_PASSWORD')
    EMAIL_BACKEND_SMTP = config('PM_EMAIL_BACKEND_SMTP')
    EMAIL_PORT = config('PM_EMAIL_PORT')
    
