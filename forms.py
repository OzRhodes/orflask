
# exploiting the forms validation libraries
# split the forms into a seperate file to enable ease of maintenance

# we write classes for forms
# pip install flask-wtf
# this also installs wtforms



from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators[DataRequired(), Length(min= 2, max = 20)])
	email = StringField('Email', validators[DataRequired(), Email()])
	password = PasswordField('Password', validators[DataRequired()])
	password_password = PasswordField('Confirm_Password', validators[DataRequired(), Equalto('password')]) 
	submit = SubmitField('Sign_up')




class LoginForm(FlaskForm):
	email = StringField('Email', validators[DataRequired(), Email()])
	password = PasswordField('Password', validators[DataRequired()])
	remember = BooleanField('Remember_Me')
	submit = SubmitField('Login')
