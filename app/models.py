from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class Pitch:(db.Model):
    '''
    Pitch class to define pitch
    '''
    all_pitches = []

    __tablename__= 'pitches'

    id = db.Column(db.Integer,primary_key=True)
    author = db.column(db.String)
    pitch_idea = db.Column(db.String)
    category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.column(db.Integer,db.ForeignKey(users.id)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(pitch_id=id).all()

        return pitches

        response = []
        for pitch in cls.all_pitches:
            if pitch.pitch_id == id:
                response.append(pitch)

        return response

    @classmethod
    def clear_pitches-(cls):
        Pitch.all_pitches.clear()

x
    def__init__(self,id,author,pitch_idea,category):

        self.id = id
        self.author = author
        self.pitch_idea = pitch_idea
        self.category = category

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.model):

   __tablename__ ='users'     

   id = db.Column(db.Integer,primary_key = True)
   username = db.Column(db.String(255),index = True)
   email = db.Column(db.String(255),unique = True,index = True)
   role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
   bio = db.Column(db.String(255))
   profile_pic_path = db.Column(db.String())
   password_hash = db.Column(db.String(255))
   password_secure = db.Column(db.String(255))
   pitches = db.relationship('Pitch',backref='user',lazy = 'dynamic')
   comments = db.relationship('Comment',backref='user',lazy = 'dynamic')


     @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User {self.username}'



class Comment (db.Model):
    '''
    class to define a persons comments
    '''
    def __init__(self,comment,author,post_posted):
        self.comment = comment
        self.author = author
        self.published = post_posted 

    all_comments =[]

    __tablename__ = 'comments'

    id = db.column(db.Integer,primary_key= True)
    comment_id = db.Column(db.Integer)
    author = db.Column(db.String)
    published = db.Column(db.DateTime,default = datetime.utcnow)
    user_id = db.Column(db.Integer.ForeignKey("users.id"))


    def save_comment(self):
        db.session.add(user)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        response = []
        comments = Comment.query.filter_by(comment_id).all()

        return comments

        for comment in cls,all_comments:
            if comment.comment_id == id:
                response.append(comment)

       return response
