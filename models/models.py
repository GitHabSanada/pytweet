from datetime import datetime
from pytweet.database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)


#Class User
#id,username,password,created_at,updated_at, age,