class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'm4CELAleo7YKYWJVkpMShg'  # import secrets; secrets.token_urlsafe(16)
    DB_NAME = 'production_db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'
    IMAGE_UPLOADS = '/Users/ervand_agadzhanyan/Desktop/Summary/Flask/lessons from Julian Nash/13. Uploading files/app/static/img/uploads'
    ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
    MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024
    SESSION_COOKIE_SECURE = True
    CLIENT_IMAGES = '/Users/ervand_agadzhanyan/Desktop/Summary/Flask/lessons from Julian Nash/14. Sending files/app/static/client/img'
    CLIENT_CSV = '/Users/ervand_agadzhanyan/Desktop/Summary/Flask/lessons from Julian Nash/14. Sending files/app/static/client/csv'
    CLIENT_REPORT = '/Users/ervand_agadzhanyan/Desktop/Summary/Flask/lessons from Julian Nash/14. Sending files/app/static/client/reports'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = 'development_db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    DB_NAME = 'production_db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'
    SESSION_COOKIE_SECURE = False
