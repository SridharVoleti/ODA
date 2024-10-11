# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,DateField,BooleanField,SubmitField,FormField,FieldList
from wtforms.validators import DataRequired,Length,Regexp,NumberRange,Optional,AnyOf
from wtforms import StringField
from app.forms.choices_config import *
from app.forms.custom_validations import *
class ShipmentDetailsFormSection(FlaskForm):

    #Form for creating a new booking with validation.

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
            AnyOf([choice[0] for choice in PACKAGE_TYPES], message="Must be a valid Clearance Place"),
            Length(max=200, message="Must have a maximum of 200 characters")
        ]
    ) 
    
    #Weight Field
    weight = IntegerField(
        'Weight',
        validators=[
            DataRequired("Weight is required"),  # Not Null validation
            NumberRange(min=1, max=1000, message="Weight must be a positive number within the allowed carrier range"),  # Positive number and within range
            validate_positive_number #Custom validation to check for positive number
        ]
    )

    # Dimensions Field
    dimensions = StringField(
        'Dimensions',  # Label for the field
        validators=[
            DataRequired("Dimensions is required"),  # Ensure the field is not empty (null)
            Regexp(r'^\d+(\.\d+)?\*\d+(\.\d+)?\*\d+(\.\d+)?$',message='Value should be in 12*15*20 format')
            # ^: Anchors the match at the beginning of the string.
            # \d+: Matches one or more digits (representing the integer part of the number).
            # (\.\d+)?: Matches an optional decimal part. The \. matches the decimal point, and \d+ matches one or more digits after the decimal. The entire group is optional due to the ?.
            # \*: Matches the literal * character separating the dimensions.
            # \d+(\.\d+)?: The same pattern is repeated for width and height.
            # $: Anchors the match at the end of the string.
            # Examples:
            # 12*15*20 → Matches
            # 12.5*15*20.1 → Matches
            # 12.5*15.5*20.5 → Matches
            # 12*15.5*20 → Matches
            # 12*15*20*25 → Doesn't match (too many dimensions)
            # 12.5.5*15*20 → Doesn't match (invalid number format)
        ],
        render_kw={"placeholder": "e.g., 12*15*20"}  # Placeholder for user guidance
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
    )

    # declared value field 
    declared_value = IntegerField(
        'Declared Value',  # Label for the field
        validators=[
            Optional(),  # Allow the field to be empty if insurance is not selected
            validate_positive_number #Custom validation to check for positive number
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
        'Bill of Ladding(BL)',
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
    cbm = IntegerField(
        'CBM',  # The label for the field
        validators=[  # A list of validators to apply to this field
            DataRequired(message="CBM is required"),  # Ensures the field is not left empty
            validate_positive_number #Custom validation to check for positive number
        ]
    )

    # 'cha' field
    cha = SelectField(
        'CHA',  # The label for the field
        choices=CHA_CHOICES,
        validators=[  # A list of validators to apply to this field
            DataRequired(message="This field is required."),  # Ensures the field is not left empty
            AnyOf(  # Ensures the selected value is one of the predefined choices
                [choice[0] for choice in CHA_CHOICES],
                message="Must be a valid CHA"
            )
        ]
    )
           

    # clearance place field 
    clearance_place = SelectField(
        'Clearance Place',
        choices=CLEARANCE_CHOICES,
        validators=[
            DataRequired(message="This field is required."),
            AnyOf([choice[0] for choice in CLEARANCE_CHOICES], message="Must be a valid Clearance Place"),
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
                regex=r'^[A-Z]{3}\d{5}$',
                message="File Reference Number must be alphanumeric (letters and numbers only)."
            )
        # ^: Anchors the match at the beginning of the string.
        # [A-Z]{3}: Matches exactly three uppercase letters (A to Z).
        # \d{5}: Matches exactly five digits (0 to 9).
        # $: Anchors the match at the end of the string.
        # Examples:
        # FRN12345 → Matches
        # REF67890 → Matches
        # ABC123 → Doesn't match (only 3 digits)
        # REF123456 → Doesn't match (6 digits instead of 5)
        # frn12345 → Doesn't match (lowercase letters)
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
    gross_weight= IntegerField(
        'Gross Weight',  # The label for the field
        validators=[  # A list of validators to apply to this field
            DataRequired(message="Gross Weight is required"),  # Ensures the field is not left empty
            validate_positive_number #Custom validation to check for positive number
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
    invoice_currency_value = IntegerField(
        'Invoice Currency Value',  # The label for the field
        validators=[  # A list of validators to apply to this field
            DataRequired(message="Gross Weight is required"),  # Ensures the field is not left empty
            validate_positive_number #Custom validation to check for positive number
        ]
    )

    # Define the invoice_type field with a SelectField and use AnyOf for validation
    invoice_type = SelectField(
        'Invoice Type',
        choices=INVOICE_TYPES, 
        validators=[
            DataRequired("invoice_type is required"),
            AnyOf(INVOICE_TYPES, message="Invalid invoice type")
        ]
    )

    # Item Description Field
    item_description = StringField('Item Description', validators=[DataRequired("item_description is required")])

    # Job Type Field
    job_type = SelectField(
        'Job Type',
        choices=JOB_TYPES,  
        validators=[
            DataRequired("invoice_type is required"),
            AnyOf(JOB_TYPES, message="Invalid Job Type")
        ]
    )

    # Nature of Contract Field
    nature_of_contract = SelectField(
        'Nature of Contract',
        choices=CONTRACT_TYPES,  
        validators=[
            DataRequired("invoice_type is required"),
            AnyOf(CONTRACT_TYPES, message="Invalid Nature of Contract")
        ]
    )

    # Nature of Payment Field
    nature_of_payment = SelectField(
        'Nature of Payment',
        choices=PAYMENT_TYPES,
        validators=[
            DataRequired("invoice_type is required"),
            AnyOf(PAYMENT_TYPES, message="Invalid Nature of Payment")
        ]
    )

    # Net Weight Field
    net_weight = IntegerField(
        'Net Weight',  # The label for the field
        validators=[  # A list of validators to apply to this field
            DataRequired(message="Gross Weight is required"),  # Ensures the field is not left empty
            validate_positive_number #Custom validation to check for positive number
        ]
    )

    # Number of Packages
    number_of_packages = IntegerField('Number of Packages', validators=[DataRequired("number_of_packages is required"),
                                                                        validate_positive_number #Custom validation to check for positive number
                                                                        ])

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
        choices=PORTS_CHOICES,
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

    # Select Job Field
    select_job = SelectField(
        'Select Job',
        choices=JOBS,  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(JOBS, message="Invalid JOB")
        ]
    )

    # SERIES Field
    series = SelectField(
        'SERIES',
        choices=SERIES,  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(SERIES, message="Invalid SERIES")
        ]
    )

    # Shipper/Exporter Field
    shipper_or_exporter = SelectField(
        'Shipper/Exporter',
        choices=EXPORTERS,  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(EXPORTERS, message="Invalid Shipper/Exporter")
        ]
    )

    # Shipping Line Field
    shipping_line = SelectField(
        'Shipping Lines',
        choices=SHIPPING_LINES,  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(SHIPPING_LINES, message="Invalid Shipping Line")
        ]
    )

    # Type of Shipment Field
    type_of_shipment = SelectField(
        'Type of Shipment',
        choices=SHIPPING_TYPES,  # Creates a list of tuples from INVOICE_TYPES
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
        choices=UNIT_TYPES,  # Creates a list of tuples from INVOICE_TYPES
        validators=[
            DataRequired("Operations Handled By is required"),
            AnyOf(UNIT_TYPES, message="Invalid Type of Shipment")
        ]
    )

    # Container Form
class ContainerDetailsFormSection(FlaskForm):
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
        ],
        render_kw={"placeholder": "e.g., 12*15*20"}  # Placeholder for user guidance
    )

    container_weight = IntegerField(
        'Container Weight',
        validators=[DataRequired("Container Weight is required")]
    )

    max_gross_weight = IntegerField(
        'Max Gross Weight',
        validators=[DataRequired('Max Gross Weight is required')]
    )

    container_seal_number = StringField(
        'Container Seal Number',
        validators=[DataRequired("Container Seal Number is required")]
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
            AnyOf([choice[0] for choice in CONTAINER_STATUS],message='Select valid Container status')
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
class ShipmentForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shipment_details = ShipmentDetailsFormSection()
        self.container_details = ContainerDetailsFormSection()

    submit = SubmitField('Submit')  # Only define this once

