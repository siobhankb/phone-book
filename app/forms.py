from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
# pip install email_validator 
from wtforms.validators import InputRequired, Email


class ContactForm(FlaskForm):
    first_name   = StringField('First Name', validators=[InputRequired()])
    last_name    = StringField('Last Name', validators=[InputRequired()])
    mobile = StringField('Mobile Phone', validators=[InputRequired()])
    work_phone = StringField('Work Phone', validators=[InputRequired()])
    email = EmailField('Email Address', validators=[Email()])
    submit = SubmitField()