from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields import EmailField
from wtforms.validators import (InputRequired, DataRequired, Email, EqualTo, ValidationError, Length)

# Creating a form for collecting contact information from users.
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        InputRequired(message="Please enter your full name")
    ])

    email = EmailField('Email Address', validators=[
        Email(message='Please enter a valid email address'),
        InputRequired(message='Please enter your e-mail address')
    ])
    subject = StringField('Subject', validators=[
        InputRequired(message="Please enter the subject for your message")
    ])

    message_area = TextAreaField('Message', render_kw={
        "rows": 8, "cols": 50
    })