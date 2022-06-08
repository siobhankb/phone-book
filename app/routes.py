from app import app
from flask import render_template, url_for, flash
from app.forms import ContactForm

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = ContactForm()
    return render_template('signup.html', form=form)