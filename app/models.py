from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin
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

    @classmethod
    def clear_pitches-(cls):
        Pitch.all_pitches.clear()

x
    def__init__(self,id,author,pitch_idea,category):

        self.id = id
        self.author = author
        self.pitch_idea = pitch_idea
        self.category = category

class User(UserMixin,db.model):

   __tablename__ ='users'     