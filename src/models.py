from datetime import datetime
from app import db  # Assuming you have already initialized SQLAlchemy as 'db' in your app package

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    profile = db.relationship('Profile', backref='user', uselist=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Profile for user {}>'.format(self.user_id)
