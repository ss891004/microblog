from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from random import Random

app = Flask(__name__)
# pip install mysql-connector-python
# app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+mysqlconnector://root:Ssmysql_1@192.168.229.128:3306/db_flask'

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+mysqldb://root:Ssmysql_1@192.168.229.128:3306/db_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True


db=SQLAlchemy(app)

migrate =Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route('/adduser/')
def add_user():
    admin = User(username='admin1', email='admin1@example.com')
    guest = User(username='guest1', email='guest1@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

    return 'add user ok'


@app.route('/')
def hello():
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True)