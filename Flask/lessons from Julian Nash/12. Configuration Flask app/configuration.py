class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'SFCSDFSDhhbyuFSEBFJHB4R9W4ABFEAW'
    DB_NAME = 'production_db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'
    UPLOADS = ''
    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = 'development_db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'

    UPLOADS = ''
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    DB_NAME = 'production_db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'
    SESSION_COOKIE_SECURE = False
