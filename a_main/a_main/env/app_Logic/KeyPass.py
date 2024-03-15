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
    CFR2_TOKEN = config('PM_CFR2_TOKEN')
    CFR2_ACC_ID = config('PM_CFR2_ACC_ID')
    CFR2_ACC_KEY = config('PM_CFR2_ACC_KEY')
    CFR2_ENDPOINT = config('PM_CFR2_ENDPOINT')
    CFR2_BUCKET = config('PM_CFR2_BUCKET')
    SHARE_GALLERY = config('SHARE_GALLERY')
    
#production    ---->
#import os
#
#class SETTINGS_KEYS:
#
#    DJANGO_KEY = os.getenv('PM_DJANGO_KEY')
#    DEBUG_STATE = os.getenv('PM_DEBUG_STATE')
#    DB_NAME = os.getenv('STDB_NAME')
#    DB_USER = os.getenv('STDB_USER')
#    DB_PASSWORD = os.getenv('STDB_PASSWORD')
#    DB_HOST = os.getenv('STDB_HOST')
#    DB_PORT = os.getenv('STDB_PORT')
#    MYSQL_ATTR_SSL_CA = os.getenv('STDB_MYSQL_ATTR_SSL_CA')
#    dbstt = os.getenv('PM_DEBUG_STATE', bool)
#    EMAIL_HOSTING = os.getenv('PM_EMAIL_HOSTING')
#    EMAIL_USER = os.getenv('PM_EMAIL_USER')
#    EMAIL_PASSWORD = os.getenv('PM_EMAIL_PASSWORD')
#    EMAIL_BACKEND_SMTP = os.getenv('PM_EMAIL_BACKEND_SMTP')
#    EMAIL_PORT = os.getenv('PM_EMAIL_PORT')
#    CFR2_TOKEN = os.getenv('PM_CFR2_TOKEN')
#    CFR2_ACC_ID = os.getenv('PM_CFR2_ACC_ID')
#    CFR2_ACC_KEY = os.getenv('PM_CFR2_ACC_KEY')
#    CFR2_ENDPOINT = os.getenv('PM_CFR2_ENDPOINT')
#    CFR2_BUCKET = os.getenv('PM_CFR2_BUCKET')
#    SHARE_GALLERY = os.getenv('ST_SHARE_GALLERY')

    
