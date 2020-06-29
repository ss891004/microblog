from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234567890POIUYTREWQ'

# from app.config import Config
# app.config.from_object(Config)

from app import routes