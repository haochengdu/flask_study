from flask import Blueprint
from chun import db
from chun import models

us = Blueprint('us', __name__)


@us.route('/index')
def index():
    # 使用SQLAlchemy在数据库中插入一条数据
    # db.session.add(models.Users(name='高件套',depart_id=1))
    # db.session.commit()
    # db.session.remove()
    result = db.session.query(models.Users).all()
    print(result)
    db.session.remove()

    return 'Index'
