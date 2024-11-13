from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(
        'email',validators=[DataRequired("email is required")]
    )

    password = PasswordField(
        'password',validators=[DataRequired("password is required")]
    )

    submit = SubmitField('login')
    