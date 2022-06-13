from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable = False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    contacts = db.relationship('Contact', backref='user') # <-- this is how to set up a foreign key!!

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<User|{self.email} /\ First|{self.id}>"

    def check_password(self, password):
        return check_password_hash(self.password, password) 

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    mobile = db.Column(db.String(17), unique=True, nullable=False)
    work_ph = db.Column(db.String(17), nullable=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #references 'user' in table 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Contact | {self.email} >< First | {self.first_name} >< Last | {self.last_name}>"

    def update(self, first_name, last_name, mobile, work_ph, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.work_ph = work_ph
        self.email = email
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
