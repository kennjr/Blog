class Config:
    """
    The general configs parent class
    """

    # SQLAlchemy = "postgresql+psycopg2://kenny:NewP@55w0rd123!@#@localhost/school"
    SECRET_KEY = "GY78JNnU1809m"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:NewPA55w0rd123)(*@localhost/pitchesdb'

class ProdConfig(Config):
    """
    Configurations for the app when it's in production mode
    Args:
        Config: The parent configuration class with General configuration settings
    """
    DEBUG = False


class DevConfig(Config):
    """
    Configurations for the app when it's in development phase/mode
    Args:
        Config: The parent configuration class with General configuration settings
    """
    # Setting the debug to True allows us to catch errors real quick
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
