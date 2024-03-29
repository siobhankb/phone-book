from app import app
from flask import render_template, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from app.forms import ContactForm, NewUserForm, LoginForm
from app.models import User, Contact


#homepage - displays user's address book
@app.route('/')
def home():
    img_url = url_for('static', filename='/tower_of_phone_books.jpg')
    if current_user.is_authenticated:
        contacts=Contact.query.filter(Contact.user_id == current_user.id).all()
        return render_template('home.html', contacts=contacts, img_url = img_url)
    else:
        return render_template('home.html', contacts=[], img_url = img_url)

#login - displays login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #find out if there is actually a user with that username & pw
        email = form.email.data
        password = form.password.data

        user = User.query.filter(User.email == email).first()

        if user is not None and user.check_password(password):
            login_user(user)
            flash(f'Welcome back, {user.email}', 'primary')
            return redirect(url_for('home'))

        flash('Incorrect username and/or password. Please try again.', 'danger')
        return redirect(url_for('login'))
    
    return render_template('login.html', form=form)

#signup - new phone book user
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
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


# add_contact page is where user can add new contact to their own phone book
@app.route('/add-contact', methods=['GET', 'POST'])
@login_required
def add_contact():
    form = ContactForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        mobile = form.mobile.data
        work = form.work_phone.data
        email = form.email.data
        user_id = current_user.id

        new_contact = Contact(first_name = first_name, last_name=last_name, mobile=mobile, work_ph=work, email=email, user_id=user_id)

        flash(f"{new_contact.first_name} {new_contact.last_name}'s contact added to Phancy Phone Book!", 'success')
        return redirect(url_for('home'))
    return render_template('new_contact.html', form=form)

@app.route('/contacts/<contact_id>')
def view_single_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id) # SELECT * FROM post WHERE id = post_id  --(post_id comes from the URL)
    return render_template('single_contact.html', contact=contact)

#edit_contact page is where logged in user can edit contact that belongs to them
@app.route('/edit-contacts/<contact_id>', methods=["GET", "POST"])
@login_required
def edit_single_contact(contact_id):
    contact_to_edit = Contact.query.get_or_404(contact_id)
    if current_user != contact_to_edit.user:
        flash("You do not have permission to edit this contact", "danger")
        return redirect(url_for('home'))
    form = ContactForm()
    if form.validate_on_submit():
        # Get form data
        new_first_name = form.first_name.data
        new_last_name = form.last_name.data
        new_mobile = form.mobile.data
        new_work = form.work_phone.data
        new_email = form.email.data
        # update the post to edit with the form data
        contact_to_edit.update(first_name=new_first_name, last_name=new_last_name, mobile=new_mobile, work_ph=new_work, email=new_email)

        flash(f'{contact_to_edit.email} has been updated', 'primary')
        return redirect(url_for('view_single_contact', contact_id=contact_to_edit.id))

    return render_template('edit_contact.html', contact=contact_to_edit, form=form)

@app.route('/delete-contacts/<contact_id>')
@login_required
def delete_contact(contact_id):
    contact_to_delete = Contact.query.get_or_404(contact_id)
    if current_user != contact_to_delete.user:
        flash("You do not have permission to delete this contact", "danger")
        return redirect(url_for('home'))
    contact_to_delete.delete()
    flash(f'Entry for {contact_to_delete.first_name} {contact_to_delete.last_name} has been deleted', 'info')
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out', 'secondary')
    return redirect(url_for('home'))