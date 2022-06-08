from flask_wtf import FlaskForm
from wtforms import FormField, StringField, IntegerField, EmailField, SubmitField
# pip install email_validator 
from wtforms.validators import InputRequired, Email

class TelephoneForm(FlaskForm):
    country_code = IntegerField('Country Code', validators=[InputRequired()])
    area_code    = IntegerField('Area Code/Exchange', validators=[InputRequired()])
    number       = StringField('Number')

class ContactForm(FlaskForm):
    first_name   = StringField('First Name', validators=[InputRequired()])
    last_name    = StringField('Last Name', validators=[InputRequired()])
    mobile_phone = StringField('Mobile Phone', validators=[InputRequired()])
    email = EmailField('Email Address', validators=[Email()])
    submit = SubmitField()