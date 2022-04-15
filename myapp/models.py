from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('FavSongs', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"


class FavSongs(db.Model):
    __tablename__ = 'song_posts'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    musician = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    releaseyear = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, musician, genre, releaseyear, text, user_id):
        self.title = title
        self.musician = musician
        self.genre = genre
        self.releaseyear = releaseyear
        self.text = text
        self.user_id = user_id
    
    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- Title: {self.Title}"