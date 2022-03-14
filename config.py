class Config:
    """
    The general configs parent class
    """

    # SQLAlchemy = "postgresql+psycopg2://kenny:NewP@55w0rd123!@#@localhost/school"
    SECRET_KEY = "GY78JNnU1809m"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:NewPA55w0rd123)(*@localhost/blogsdb'

class ProdConfig(Config):
    """
    Configurations for the app when it's in production mode
    Args:
        Config: The parent configuration class with General configuration settings
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://afkoryyclozwlw:4b2fbe987462b592f96118c52ae8cd2f622c82d56d74c18c5106ac0c0efe446e@ec2-3-222-204-187.compute-1.amazonaws.com:5432/d88sj205t9jgec'


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
