from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    username = StringField(
        'username',validators=[DataRequired("username is required")]
    )

    password = PasswordField(
        'password',validators=[DataRequired("password is required")]
    )

    submit = SubmitField('login')
    