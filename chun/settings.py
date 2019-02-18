from redis import Redis


class BaseConfig(object):
    # Flask-Session: 第二步配置
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = Redis(host='192.168.0.94', port='6379')

    # ##### SQLALchemy配置文件 #####
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/s9day122?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_MAX_OVERFLOW = 5

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    pass


class ProConfig(BaseConfig):
    pass
