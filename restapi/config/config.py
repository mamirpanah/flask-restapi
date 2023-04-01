from os import environ

class Config:

    ########################## Application Config ##########################

    ENV = environ.get("RESTAPI_APP_ENV", "production")
    
    DEBUG = bool(int(environ.get("RESTAPI_APP_DEBUG", "0")))
    
    TESTING = bool(int(environ.get("RESTAPI_APP_TESTING", "0")))
    
    SECRET_KEY = environ.get("RESTAPI_APP_SECRET_KEY", "HARD-HARD-HARD-SECRET-KEY")

    TIMEZONE = environ.get("RESTAPI_APP_TIMEZONE", "Asia/Tehran")

