from app import app
from flask import render_template, url_for, redirect, flash
from flask_login import login_user#, login_required, logout_user
from app.forms import AddContactForm, NewUserForm, LoginForm
from app.models import User, Contact

#homepage - displays user's address book
@app.route('/home')
def home():
    contacts=Contact.query.all()
    return render_template('home.html', contacts=contacts)

#login - displays login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #find out if there is actually a user with that username & pw
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user is not None and user.check_password(password):
            login_user(user)
            flash(f'Welcome back, {user.email}', 'primary')
            return redirect(url_for('home'))

        flash('Incorrect username and/or password. Please try again.', 'danger')
        return redirect(url_for('login'))
    
    return render_template('login.html', form=form)

#signup - new phone book owner/user
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = NewUserForm()
    if form.validate_on_submit():
        print('This was a huge success')
        email = form.email.data
        password = form.password.data
        # Query user table to make sure info entered is unique
        user_check = User.query.filter((User.email == email)).all()
        if user_check:
            flash('A user with that username or email already exitsts', 'danger')
            return redirect(url_for('signup'))

        # add the user to the database
        new_user = User(email=email, password=password)
        
        # show message of success/failure
        flash(f'{new_user.email} has successfully signed up!', 'success')
        #redirect back to the homepage
        return redirect(url_for('add_contact'))

    return render_template('signup.html', form=form)

# add_contact page is where user can add new contact to their own phone book
@app.route('/add-contact', methods=['GET', 'POST'])
def add_contact():
    form = AddContactForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        mobile = form.mobile.data
        work = form.work_phone.data
        email = form.email.data
        duplicate_check = Contact.query.filter((Contact.email == email)|(Contact.mobile== mobile)).all()
        if duplicate_check:
            flash(f'An entry for{first_name} {last_name} already exits.', 'warning')
            return redirect(url_for('signup'))
        
        new_contact = Contact(first_name = first_name, last_name=last_name, mobile=mobile, work_ph=work, email=email)

        flash(f"{new_contact.first_name} {new_contact.last_name}'s contact added to Phancy Phone Book!", 'success')
        return redirect(url_for('add_contact'))
    return render_template('new_contact.html', form=form)
