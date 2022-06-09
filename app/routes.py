from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import ContactForm
from app.models import Contact

@app.route('/home')
def home():
    contacts=Contact.query.all()
    return render_template('home.html', contacts=contacts)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = ContactForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        mobile = form.mobile.data
        work = form.work_ph.data
        email = form.email.data
        duplicate_check = Contact.query.filter((Contact.email == email)|(Contact.mobile== mobile)).all()
        if duplicate_check:
            flash(f'An entry for{first_name} {last_name} already exits.', 'warning')
            return redirect(url_for('signup'))
        new_contact = Contact(first_name = first_name, last_name=last_name, mobile=mobile, work=work, email=email)
        flash(f"{new_contact.first_name} {new_contact.last_name}'s contact added to Phancy Phone Book!", 'success')
        return redirect(url_for('signup'))
    return render_template('signup.html', form=form, new_contact=new_contact)


