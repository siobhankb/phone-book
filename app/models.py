from app import db
from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.String(17), nullable=False)
    work_ph = db.Column(db.String(17), nullable=True)
    email = db.Column(db.String(50), nullable=False)
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Contact|{self.title} /\ First|{self.first_name} /\ Last|{self.last_name}>"