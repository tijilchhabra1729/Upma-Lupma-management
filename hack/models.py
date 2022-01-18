from hack import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    fname = db.Column(db.String)
    email = db.Column(db.String(64),index=True)
    roles = db.Column(db.String(64))

    password_hash = db.Column(db.String)
    def __init__(self,email,roles,fname,password):
        self.fname=fname
        self.email = email
        self.roles = roles
        self.password_hash = generate_password_hash(password)


    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class Raw(db.Model):
    __tablename__ = 'raw'
    id = db.Column(db.Integer , primary_key = True)
    beans = db.Column(db.Integer,nullable = True)
    milk = db.Column(db.Integer,nullable = True)
    sugar = db.Column(db.Integer,nullable = True)
    date = db.Column(db.DateTime,nullable = True)

    def __init__(self,beans,milk,sugar,date):
        self.beans = beans
        self.sugar = sugar
        self.milk = milk
        self.date = date

class Manufacture(db.Model):
    __tablename__ = 'manufacture'
    id = db.Column(db.Integer , primary_key = True)
    beans = db.Column(db.Integer,nullable = True)
    milk = db.Column(db.Integer,nullable = True)
    sugar = db.Column(db.Integer,nullable = True)

    defected = db.Column(db.Integer)
    perfect = db.Column(db.Integer)
    date = db.Column(db.DateTime,nullable = True)

    def __init__(self,defected,perfect,date,beans,milk,sugar):
        self.perfect =perfect
        self.defected = defected
        self.beans = beans
        self.sugar = sugar
        self.milk = milk
        self.date = date

class Sell(db.Model):
    __tablename__ = 'sell'
    id = db.Column(db.Integer , primary_key = True)
    offline = db.Column(db.Integer,nullable = True)
    online = db.Column(db.Integer,nullable = True)
    buisness = db.Column(db.Integer,nullable = True)

    date = db.Column(db.DateTime,nullable = True)

    def __init__(self,offline,online,buisness,date):
        self.offline = offline
        self.online = online
        self.buisness = buisness
        self.date = date
