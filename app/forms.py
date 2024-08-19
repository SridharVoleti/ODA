# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BookingForm(FlaskForm):
    """
    Form for creating a new booking with validation.
    """
    shipment_id = StringField('Shipment ID', validators=[DataRequired()])
    shipping_company = StringField('Shipping Company', validators=[DataRequired()])
    sender_name = StringField('Sender Name', validators=[DataRequired()])
    sender_address = StringField('Sender Address', validators=[DataRequired()])
    consignee = StringField('Consignee', validators=[DataRequired()])
    consignee_address = StringField('Consignee Address', validators=[DataRequired()])
    package_type = StringField('Package Type', validators=[DataRequired()])
    submit = SubmitField('Submit')
