from flask import Flask
from flask_session import Session

# 第一步：导入并实例化SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .views.account import ac
from .views.user import us

from .models import *


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.ProConfig')

    app.register_blueprint(ac)
    app.register_blueprint(us)

    # Flask-Session: 第一步示例Session
    # Session(app)

    # 第三步：依赖app中的配置文件,对sqlalchemy的配置
    db.init_app(app)

    return app
