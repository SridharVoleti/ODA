from wtforms import SelectField,StringField,IntegerField,DateField,SubmitField
from wtforms.validators import DataRequired,AnyOf,Regexp
from flask_wtf import FlaskForm
from app.forms.choices_config import *

class ContainerForm(FlaskForm):
    container_type = SelectField(
    'Container Type',
    choices=CONTAINER_TYPES,
    validators=[DataRequired("Container Type is required"),
                AnyOf([choice[0] for choice in CONTAINER_TYPES],message="select valid contaier type")
                ]
    )

    container_size = StringField(
        'Container Size',
        validators=[DataRequired('Container Size is required'),
            Regexp(r'^\d+(\.\d+)?\*\d+(\.\d+)?\*\d+(\.\d+)?$' , message="Invalid format")
            # Must be in format: number*number*number
        ]
    )

    container_weight = IntegerField(
        'Container Weight',
        validators=[DataRequired("Container Weight is required")]
    )

    max_gross_weight = IntegerField(
        'Max Gross Weight',
        validators=[DataRequired('Max Gross Weight is required')]
    )

    # Owner/Operator Code
    owner_or_operator_code = StringField(
        'Owner/Operator Code',
        validators=[DataRequired("Owner/Operator Code is required")]
    )

    container_status = SelectField(
        'Container Status',
        choices=CONTAINER_STATUS,
        validators=[DataRequired('Container Status is required'),
            AnyOf([choice for choice in CONTAINER_STATUS],message='Select valid Container status')
        ]
    )

    iso_code = StringField(
        'ISO CODE',
        validators=[DataRequired('ISO CODE is required')]
    )

    container_condtition = SelectField(
        'Container Condition',
        choices=CONTAINER_CONDITION,
        validators=[
            AnyOf([choice for choice in CONTAINER_CONDITION],message='Select valid Container condition')
        ]

    )

    date_of_manufacture = DateField(
        'Date of Manufacture',
        validators=[DataRequired('Date of Manufacture is required')]
    )

    last_date_inspection = DateField(
        'Last Inspection Date',
        validators=[DataRequired('Last Inspection Date is required')]
    )

    cargo_type = SelectField(
        'Cargo type',
        choices=CARGO_TYPES,
        validators=[
            DataRequired('Cargo type is required'),
            AnyOf([choice for choice in CARGO_TYPES],message='Select valid Cargo type')
        ]
    )

    submit = SubmitField('Next')