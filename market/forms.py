from flask_wtf import FlaskForm
from market.models import User, Item
from wtforms import StringField , PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
    def validate_email_address(self, email_to_check):
        email_address = User.query.filter_by(email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different Email Address')


    username  = StringField(label='User Name:',validators=[Length(min=2, max=20), DataRequired()])
    email_address  = StringField(label='Email:', validators=[Email(),  DataRequired()])
    password1 = PasswordField(label='Pasword:', validators=[Length(min=6),  DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'),  DataRequired()])
    submit = SubmitField(label='Create Account')
#Login Form
class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')

#Item Purchase Confirmation

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item!")

#Item Sell

class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item!")
