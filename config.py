class BaseConfig:
    SECRET_KEY = "FLASK123"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/testwebsys?charset=utf8mb4"

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/testwebsys?charset=utf8mb4"

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/testwebsys?charset=utf8mb4"
