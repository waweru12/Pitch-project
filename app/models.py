from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitcher = db.relationship("Pitch", backref= "user", lazy="dynamic")
    reviews = db.relationship("Review", backref = "user", lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'
    

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

 

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(255))
    title = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    reviews = db.relationship("Review", backref = "pitch", lazy = "dynamic")
    pitch_statement = db.Column(db.String())
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()




class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
    pitch_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_review(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_reviews(cls, id):
        reviews = Review.query.filter_by(pitch_id = id).all()
        return reviews

