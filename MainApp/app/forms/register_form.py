from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired,AnyOf

ROLE_CHOICES = ['Admin','Shipper','Forwarder']

class RegisterForm(FlaskForm):
    firstname = StringField(
        'First Name',validators=[DataRequired("firstname is required")]
    )
    middlename = StringField(
        'Middle Name'
    )
    lastname = StringField(
        'Last Name',validators=[DataRequired("lastname is required")]
    )
    address = StringField(
        'Address',validators=[DataRequired("address is required")]
    )
    phone = StringField(
        'Phone Number',validators=[DataRequired("phone is required")]
    )
    username = StringField(
        'username',validators=[DataRequired("username is required")]
    )

    password = PasswordField(
        'password',validators=[DataRequired("password is required")]
    )
    role = SelectField(
        'Role',
        choices=['Admin','Shipper','Forwarder'],
        validators=[ DataRequired('Role is required'),
                   AnyOf([choice for choice in ROLE_CHOICES])
                     ]
    )

    submit = SubmitField('Register')
    