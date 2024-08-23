# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,DateField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Regexp,NumberRange,Optional,AnyOf
from wtforms import StringField
from datetime import datetime 
from app.forms.choices_config import *
from app.forms.custom_validations import *
class BookingForm(FlaskForm):
    """
    Form for creating a new booking with validation.
    """
    # Shipment Id Field
    shipment_id = StringField('Shipment ID', validators=[DataRequired("shipment_id is required"), # Not Null validation
    Regexp(r'^[a-zA-Z0-9]+$', message="Must be alphanumeric") # Alpha Numeric validation
    ])

    # Shipping Company Field
    shipping_company = StringField(
        'Shipping Company',
        validators=[
            DataRequired("Shipping company is required"),  # Not Null validation
            Length(max=200, message="Must have a maximum of 200 characters"),  # Maximum 200 characters
            Regexp(r'^[a-zA-Z0-9]+$', message="Must be alphanumeric")  # Alpha Numeric validation
        ]
    )

    # Sender Name Field
    sender_name = StringField(
        'Sender Name',
        validators=[
            DataRequired("Sender name is required"),  # Not Null validation
            Length(max=50, message="Must have a maximum of 50 characters"),  # Maximum 50 characters
        ]
    )

    # Sender Address Field
    sender_address = StringField(
        'Sender Address',
        validators=[
            DataRequired("Sender address is required"),  # Not Null validation
            Regexp(
                r'^[a-zA-Z0-9\s,.-]+$',
                message="Must be a valid address format"
            )  # Valid Address Format validation
        ]
    )

    # Consignee Field
    consignee = StringField(
        'Consignee',
        validators=[
            DataRequired("Consignee is required"),  # Not Null validation
            Length(max=200, message="Must have a maximum of 200 characters"),  # Maximum 200 characters
        ]
    )

    # Consignee Address Field
    consignee_address = StringField(
        'Consignee Address',
        validators=[
            DataRequired("Consignee address is required"),  # Not Null validation
            Regexp(
                r'^[a-zA-Z0-9\s,.-]+$',
                message="Must be a valid address format"
            )  # Valid Address Format validation
        ]
    )

    #Package Field
    package_type = SelectField(
        'Package Types',
        choices=PACKAGE_TYPES,
        validators=[
            DataRequired(message="This field is required."),
            AnyOf([choice for choice in PACKAGE_TYPES], message="Must be a valid Clearance Place"),
            Length(max=200, message="Must have a maximum of 200 characters")
        ]
    ) 
    
    #Weight Field
    weight = IntegerField(
        'Weight',
        validators=[
            DataRequired("Weight is required"),  # Not Null validation
            NumberRange(min=1, max=1000, message="Weight must be a positive number within the allowed carrier range")  # Positive number and within range
        ]
    )

    # Dimensions Field
    dimensions = StringField(
        'Dimensions',  # Label for the field
        validators=[
            DataRequired("Dimensions is required"),  # Ensure the field is not empty (null)
            validate_positive_number  # Use the custom validator to check for a positive number
        ]
    )

    # Define the 'shipping_date' field as a DateField
    shipping_date = DateField(
        'Shipping Date',  # Label for the field
        validators=[
            DataRequired("Must be a valid date")  # Ensure the field is not empty and contains a valid date
        ]
    )

    # Define the 'delivery_date' field as a DateField
    delivery_date = DateField(
        'Delivery Date',  # Label for the field
        validators=[
            DataRequired("Must be a valid date"),  # Ensure the field is not empty and contains a valid date
            validate_future_date  # Use the custom validator to check that the date is in the future
        ]
    )

    # Define the 'shipping_method' field as a StringField
    shipping_method = SelectField(
        'Shipping Methods',
        choices=SHIPPING_METHODS,
        validators=[
            DataRequired(message="This field is required."),
            AnyOf([choice for choice in SHIPPING_METHODS], message="Must be a valid  shipping method"),
            Length(max=200, message="Must have a maximum of 200 characters")
        ]
    ) 

    # insurance field
    insurance = BooleanField(
        'Insurance',  # Label for the field
        validators=[
            DataRequired("Must be a boolean value")  # Ensure the field is not empty and contains a valid boolean value (True/False)
        ]
    )

    # declared value field 
    declared_value = IntegerField(
        'Declared Value',  # Label for the field
        validators=[
            Optional(),  # Allow the field to be empty if insurance is not selected
            validate_declared_value  # Apply the custom validator to check the condition
        ]
    )

    # special instructions field 
    special_instructions = StringField(
        'Special Instructions',  # Label for the field
        validators=[
            Optional(),  # Make the field optional; it can be left empty
            Length(max=200, message="Must have a maximum of 200 characters")  # Ensure the input text does not exceed 200 characters
        ]
    )

    # bill_of_lading' field 
    bill_of_lading = SelectField(
        'Bill of Ladinf(BL)',
        choices=BL_TYPES,
        validators=[
            DataRequired(message="This field is required."),
            AnyOf([choice for choice in BL_TYPES], message="Must be a valid Clearance Place"),
            Length(max=200, message="Must have a maximum of 200 characters")
        ]
    ) 
    

    # carting point field
    carting_point = StringField(
        'Carting Point',  # The label for the field
        validators=[  # A list of validators to apply to this field
            DataRequired(message="Carting Point is required"),  # Ensures the field is not left empty
             Regexp(
                r'^[a-zA-Z0-9\s,.-]+$',
                message="Must be a valid address format"
            )  # Valid Address Format validation
        ]
    )
    
    # 'cbm' field
    cbm = StringField(
        'CBM',  # The label for the field
        validators=[  # A list of validators to apply to this field
            DataRequired(message="CBM is required"),  # Ensures the field is not left empty
            validate_positive_number  # Applies the custom positive number validation logic
        ]
    )

    # 'cha' field
    cha = SelectField(
        'CHA',  # The label for the field
        choices=[  # Predefined choices for the SelectField
            ('ABC Customs Services Ltd', 'ABC Customs Services Ltd'),
            ('Global Trade Brokers Inc', 'Global Trade Brokers Inc'),
            ('XYZ Logistics and Customs', 'XYZ Logistics and Customs')
        ],
        validators=[  # A list of validators to apply to this field
            DataRequired(message="This field is required."),  # Ensures the field is not left empty
            AnyOf(  # Ensures the selected value is one of the predefined choices
                ['ABC Customs Services Ltd', 'Global Trade Brokers Inc', 'XYZ Logistics and Customs'],
                message="Must be a valid CHA"
            )
        ]
    )
           

    # clearance place field 
    clearance_place = SelectField(
        'Clearance Place',
        choices=PREDEFINED_CHOICES,
        validators=[
            DataRequired(message="This field is required."),
            AnyOf([choice[0] for choice in PREDEFINED_CHOICES], message="Must be a valid Clearance Place"),
            Length(max=200, message="Must have a maximum of 200 characters")
        ]
    )  
   
    # Co-Loader Field
    co_loader = StringField('Co-Loader',validators=[DataRequired("Co-Loader is required")])
    
    # Container Stuffing
    container_stuffing = StringField('Container Stuffing',validators=[DataRequired("Co-Loader is required")])
    
    # Define the 'file_reference_number' field as a StringField
    file_reference_number = StringField(
        'File Reference Number',  # The label for the field
        validators=[
            DataRequired(message="File Reference Number is required"),  # Ensures the field is not left empty
            Regexp(  # Regex to ensure the value is alphanumeric
                regex=r'^[a-zA-Z0-9]+$',
                message="File Reference Number must be alphanumeric (letters and numbers only)."
            )
        ])

    # Define the 'forwarder' field as a StringField
    forwarder = StringField(
        'Forwarder',  # The label for the field
        validators=[
            DataRequired(message="Forwarder is required"),  # Ensures the field is not left empty
            Regexp(  # Regex to ensure the value is text (letters, spaces, and common punctuation)
                regex=r'^[a-zA-Z0-9 .,&\']+$',
                message="Forwarder must contain only letters, numbers, spaces, and common punctuation."
            ),
            Length(max=200, message="Forwarder must be less than 200 characters.")  # Ensures the input does not exceed 200 characters
        ]
    )

    # Define the 'fpod' field as a StringField
    fpod = StringField(
        'FPOD',  # The label for the field
        validators=[
            DataRequired(message="FPOD is required"),  # Ensures the field is not left empty
            Regexp(  # Regex to ensure the value is valid text (letters, spaces, and common punctuation)
                regex=r'^[a-zA-Z0-9 .,&\']+$',
                message="FPOD must contain only letters, numbers, spaces, and common punctuation."
            ),
            Length(max=200, message="FPOD must be less than 200 characters.")  # Ensures the input does not exceed 200 characters
        ]
    )

    # Gross Weight Field
    gross_weight= StringField(
        'Gross Weight',  # The label for the field
        validators=[  # A list of validators to apply to this field
            DataRequired(message="Gross Weight is required"),  # Ensures the field is not left empty
            validate_positive_number  # Applies the custom positive number validation logic
        ]
    )

    # Invoice Currency Field
    invoice_currency = SelectField(
        'Invoice Currency',
        choices=[(choice, choice) for choice in CURRENCY_CHOICES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("invoice_type is required"),
            AnyOf(CURRENCY_CHOICES, message="Invalid invoice type")
        ]
    )

    # Invoice Currency Value Field
    invoice_currency_value = StringField(
        'Invoice Currency Value',  # The label for the field
        validators=[  # A list of validators to apply to this field
            DataRequired(message="Gross Weight is required"),  # Ensures the field is not left empty
            validate_positive_number  # Applies the custom positive number validation logic
        ]
    )

    # Invoice Date Field
    invoice_date= DateField(
        'Invoice Date',  # Label for the field
        validators=[
            DataRequired("Must be a valid date")  # Ensure the field is not empty and contains a valid date
        ]
    )

    # Defining the invoice_number field as a StringField with two validators
    invoice_number = StringField(
        'Invoice Number',  # Label for the form field
        validators=[
            # First validator ensures that the field is not empty
            DataRequired("invoice_number is required"),
            # Second validator enforces the specific format using a regular expression
            Regexp(
                r'^INV-\d{6}-[A-Z]{3}-\d+$',  # Regex pattern to match the format INV-YYMMDD-CLI-1            
                # Custom error message to be shown if the input doesn't match the pattern
                message=("Invalid format for invoice number. The correct format is "
                         "INV-YYMMDD-CLI-1, e.g., INV-240823-CLI-1.")
            )
        ]
    )



    # Define the invoice_type field with a SelectField and use AnyOf for validation
    invoice_type = SelectField(
        'Invoice Type',
        choices=[(choice, choice) for choice in INVOICE_TYPES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("invoice_type is required"),
            AnyOf(INVOICE_TYPES, message="Invalid invoice type")
        ]
    )

    # Item Description Field
    item_description = StringField('Item Description', validators=[DataRequired("item_description is required")])

    #Job Date Field
    job_date = DateField(
        'Job Date',  # Label for the field
        validators=[
            DataRequired("Must be a valid date")  # Ensure the field is not empty and contains a valid date
        ]
    )

    # job Number field 
    job_number = StringField(
        'Job Number',
        validators=[
            DataRequired("job_number is required"),  # Ensure the field is not left empty
            Regexp(
                r'^[A-Za-z0-9]+$',  # Regex pattern to match alphanumeric characters only
                message="Job number must be alphanumeric (letters and numbers only)."
            )
        ]
    )

    # Job Type Field
    job_type = SelectField(
        'Job Type',
        choices=[(choice, choice) for choice in JOB_TYPES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("invoice_type is required"),
            AnyOf(JOB_TYPES, message="Invalid Job Type")
        ]
    )

    # Nature of Contract Field
    nature_of_contract = SelectField(
        'Nature of Contract',
        choices=[(choice, choice) for choice in CONTRACT_TYPES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("invoice_type is required"),
            AnyOf(CONTRACT_TYPES, message="Invalid Nature of Contract")
        ]
    )

    # Nature of Payment Field
    nature_of_payment = SelectField(
        'Nature of Payment',
        choices=[(choice, choice) for choice in PAYMENT_TYPES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("invoice_type is required"),
            AnyOf(PAYMENT_TYPES, message="Invalid Nature of Payment")
        ]
    )

    # Net Weight Field
    net_weight = StringField(
        'Invoice Currency Value',  # The label for the field
        validators=[  # A list of validators to apply to this field
            DataRequired(message="Gross Weight is required"),  # Ensures the field is not left empty
            validate_positive_number  # Applies the custom positive number validation logic
        ]
    )

    # Number of Packages
    number_of_packages = IntegerField('Number of Packages', validators=[DataRequired("number_of_packages is required")])

    # Operations Handled By Field
    operation_handle_by = SelectField(
        'Nature of Payment',
        choices=[(choice, choice) for choice in OPERATION_HANDLED_BY],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(OPERATION_HANDLED_BY, message="Invalid Operation team")
        ]
    )

    # Plan Date Field
    plan_date = DateField(
        'Plan Date',  # Label for the field
        validators=[
            DataRequired("Must be a valid date")  # Ensure the field is not empty and contains a valid date
        ]
    )

    # Port of Discharge Field
    pod = SelectField(
        'Port of Discharge',
        choices=[(choice, choice) for choice in PORTS_CHOICES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(PORTS_CHOICES, message="Invalid Port")
        ]
    )

    # Port of Landing Field
    pol = SelectField(
        'Port of Landing',
        choices=[(choice, choice) for choice in PORTS_CHOICES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(PORTS_CHOICES, message="Invalid Port")
        ]
    )

    # Port of Reciept Field
    por = SelectField(
        'Port of Reciept',
        choices=[(choice, choice) for choice in PORTS_CHOICES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(PORTS_CHOICES, message="Invalid Port")
        ]
    )

    # Remarks Field
    remarks = StringField('Remarks', validators=[DataRequired("remarks is required")])

    # Sales Person Field
    sales_person_name = StringField('Sales Person Name', validators=[DataRequired("sales_person_name is required")])

    # Define the sb_number field with a StringField and validators
    sb_number = StringField(
        'SB Number',
        validators=[
            DataRequired("sb_number is required"),  # Ensure the field is not left empty
            Regexp(
                r'^SB\d+$',  # Regex pattern to match 'SB' followed by one or more digits
                message="SB number must start with 'SB' followed by digits."
            )
        ]
    )

    # SB Number Date Field
    sb_number_date = DateField(
        'SB Number Date',  # Label for the field
        validators=[
            DataRequired("Must be a valid date")  # Ensure the field is not empty and contains a valid date
        ]
    )

    # Select Job Field
    select_job = SelectField(
        'Select Job',
        choices=[(choice, choice) for choice in JOBS],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(JOBS, message="Invalid JOB")
        ]
    )

    # SERIES Field
    series = SelectField(
        'SERIES',
        choices=[(choice, choice) for choice in SERIES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(SERIES, message="Invalid SERIES")
        ]
    )

    # Shipper/Exporter Field
    shipper_or_exporter = SelectField(
        'Shipper/Exporter',
        choices=[(choice, choice) for choice in EXPORTERS],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(EXPORTERS, message="Invalid Shipper/Exporter")
        ]
    )

    # Shipping Line Field
    shipping_line = SelectField(
        'Shipping Lines',
        choices=[(choice, choice) for choice in SHIPPING_LINES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(SHIPPING_LINES, message="Invalid Shipping Line")
        ]
    )

    # Type of Shipment Field
    type_of_shipment = SelectField(
        'Type of Shipment',
        choices=[(choice, choice) for choice in SHIPPING_TYPES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(SHIPPING_TYPES, message="Invalid Type of Shipment")
        ]
    )

    # unit Field
    unit = StringField('Unit', validators=[DataRequired("unit_type is required")])

    # Unit Field
    unit_type = SelectField(
        'Unit Type',
        choices=[(choice, choice) for choice in UNIT_TYPES],  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(UNIT_TYPES, message="Invalid Type of Shipment")
        ]
    )

    submit = SubmitField('Next')