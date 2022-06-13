from app import app, db
from app.models import Contact

@app.shell_context_processor
def make_context():
    return {'db':db, 'Contact': Contact}

@app.before_first_request
def create_tables():
    db.create_all()