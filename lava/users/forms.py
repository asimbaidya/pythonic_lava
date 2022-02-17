from tokenize import String
from flask_wtf import FlaskForm
from wtforms import (StringField,
    PasswordField,
    SelectField,
    SubmitField,
    DateField,
    BooleanField,
    )
from wtforms.validators import (DataRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
    )

from lava.models import User

class RegistatonForm(FlaskForm):
    name = StringField('Name',
            validators=[DataRequired(),Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password',
        validators=[DataRequired(),EqualTo('password')])
    gender = SelectField('Gender',
       choices = [('M', 'Male'), ('F', 'Female'),('O','Other')])
    b_date = DateField('Birth Date')
    submit = SubmitField('Register')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError(f"Choose a different email address!!")


    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
    