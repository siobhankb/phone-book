from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_shhh'

from . import routes