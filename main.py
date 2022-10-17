from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(70), unique=True)
    password = db.Column(db.Text)


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(config['development'])
    config['development'].init_app(app)
    db.init_app(app)
    app.run()
