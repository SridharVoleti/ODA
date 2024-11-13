from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired,AnyOf

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
    email = StringField(
        'email',validators=[DataRequired("email is required")]
    )

    password = PasswordField(
        'password',validators=[DataRequired("password is required")]
    )
    role = StringField(
        'Role',
        validators=[ DataRequired('Role is required')]
    )

    submit = SubmitField('Register')
    