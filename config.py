import os


class Config:
    """
    General configuration parent class
    """

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    SECRET_KEY = os.urandom(32)
    
    SQLALCHEMY_DATABASE_URI ="postgresql+psycopg2://moringa:kodhanjo@localhost:pitching"

    # email configurations
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    """
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG=False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ="postgresql+psycopg2://moringa:kodhanjo@localhost/pitching_test"


class DevConfig(Config):
    """
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:kodhanjo@localhost/pitching"
    DEBUG = True


# DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig,
}
