from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired,AnyOf

USER_ROLES = ["Admin","Shipper","Forwarder","Customer"]

class InviteForm(FlaskForm):
    email = StringField(
        'email',validators=[DataRequired("email is required")]
    )

    role = SelectField(
        'Role',
        choices=USER_ROLES,
        validators=[AnyOf([choice for choice in USER_ROLES],message="Select a valid role"),DataRequired("Role is required")]
    )

    submit = SubmitField('Send Invitation')
    