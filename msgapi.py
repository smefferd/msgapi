import argparse
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSAPI, SAFRSBase


def parse_args():
    parser = argparse.ArgumentParser(description='HTTP API Messaging Service')
    parser.add_argument('--host', default='localhost',
                        help='hostname of http service')
    parser.add_argument('--port', type=int, default='5000',
                        help='tcp port for http service')
    parser.add_argument('--prefix', default='',
                        help='api endpoint url prefix for http service')
    parser.add_argument('--db', default='sqlite://',
                        help='database connection uri')
    parser.add_argument('--add-test-data', default=True, dest='testdata',
                        help='add bob and jane users with existing messages')
    return parser.parse_args()


db = SQLAlchemy()


class User(SAFRSBase, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    registration_date = db.Column(db.DateTime)


class Message(SAFRSBase, db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    sender = db.relationship(User, foreign_keys='Message.sender_id')
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    send_time = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String, nullable=False)

    @classmethod
    def filter(cls, arg):
        """
        Custom filter method to return messages by recipient_id and optionally sender_id
        :param arg: recipient_id [,sender_id]
        """
        filter_args = arg.split(',')
        recipient_id = filter_args[0]
        sender_id = filter_args[1] if len(filter_args) > 1 else None
        print ('recipient_id: {}, sender_id: {}'.format(recipient_id, sender_id))
        if sender_id is not None:
            return Message.query.filter_by(recipient_id=recipient_id, sender_id=sender_id)
        else:
            return Message.query.filter_by(recipient_id=recipient_id)


def add_test_data():
    User(id=1, name="Bob", registration_date=datetime.now())
    User(id=2, name="Jane", registration_date=datetime.now())
    Message(message="Hey I just joined msgapi! Lol!", recipient_id=1, sender_id=2, send_time=datetime.now())
    db.session.commit()


def create_app():
    app = Flask(__name__)
    app.config.update(SQLALCHEMY_DATABASE_URI=args.db)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
        if args.testdata:
            add_test_data()
        api = SAFRSAPI(app, host=args.host, port=args.port, prefix=args.prefix)
        api.expose_object(User)
        api.expose_object(Message)
        return app


args = parse_args()
app = create_app()
print("API can be accessed with the url: http://{}:{}/{}".format(args.host, args.port, args.prefix))
app.run(host=args.host)
