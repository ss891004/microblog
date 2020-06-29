from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from flask import Flask
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
import uuid


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

def show_users():
    with db.app.app_context():
        print(User.query.all())


class Config(object):
    JOBS = [
        {
            'id': str(uuid.uuid1()),
            'func': show_users,
            'trigger': 'interval',
            'seconds': 2
        }
    ]

    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url='mysql+mysqldb://root:Ssmysql_1@192.168.229.128:3306/db_flask')
    }

    SQLALCHEMY_DATABASE_URI ='mysql+mysqldb://root:Ssmysql_1@192.168.229.128:3306/db_flask'

    SCHEDULER_API_ENABLED = True


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())

    db.app = app
    db.init_app(app)

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    app.run()