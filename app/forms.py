from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class SignUpForm(FlaskForm):
    username = StringField(label='Pokemon_name', validators=[DataRequired()])
    email = StringField("Email", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    confirm_password = PasswordField("Confirm your password", [DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField(label='Pokemon_name', validators=[DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField()

