from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import ContactForm

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = ContactForm()
    if form.validate_on_submit():
        print('Okie dokie, artichokie')
        flash('Contact successfully added!', 'success')
        return redirect(url_for('signup'))
    return render_template('signup.html', form=form)