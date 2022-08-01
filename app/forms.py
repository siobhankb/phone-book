from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
# pip install email_validator 
from wtforms.validators import DataRequired, Email, EqualTo

class NewUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

class ContactForm(FlaskForm):
    first_name   = StringField('First Name', validators=[DataRequired()])
    last_name    = StringField('Last Name', validators=[DataRequired()])
    mobile = StringField('Mobile', validators=[DataRequired()])
    work_phone = StringField('Work', validators=[DataRequired()])
    email = EmailField('Email', validators=[Email()])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('User email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()