# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,DateField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Regexp,NumberRange,Optional,AnyOf
from wtforms import StringField, ValidationError
from datetime import datetime 

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
        'Shipping Company ID',
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
            Regexp(r'^[a-zA-Z0-9]+$', message="Must be alphanumeric")  # Alpha Numeric validation
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
            Regexp(r'^[a-zA-Z0-9]+$', message="Must be alphanumeric")  # Alpha Numeric validation
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
        'Package Type',
        choices=[
            ('Option1', 'Option1'),
            ('Option2', 'Option2'),
            ('Option3', 'Option3')
        ],
        validators=[
            DataRequired(message="Package type is required."),  # Ensures a selection is made
            AnyOf(['Option1', 'Option2', 'Option3'], message="Must be a valid Package Type.")  # Validates selection
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
    # Define a custom validator to check if the input is a positive number
    def validate_positive_number(form, field):
        try:
            # Attempt to convert the field's data to a float
            value = float(field.data)
            # Raise a validation error if the value is not positive
            if value <= 0:
                raise ValidationError("Dimensions must be a positive number.")
        except ValueError:
            # Raise a validation error if the conversion to float fails (input is not a number)
            raise ValidationError("Dimensions must be a positive number.")
    # Define the 'dimensions' field as a StringField
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

    # Define a custom validator to check if the date is in the future
    def validate_future_date(form, field):
        if field.data <= datetime.today().date():  # Check if the date is today or in the past
            raise ValidationError("Delivery date must be in the future.")  # Raise an error if the date is not in the future
    # Define the 'delivery_date' field as a DateField
    delivery_date = DateField(
        'Delivery Date',  # Label for the field
        validators=[
            DataRequired("Must be a valid date"),  # Ensure the field is not empty and contains a valid date
            validate_future_date  # Use the custom validator to check that the date is in the future
        ]
    )

    # Define the 'shipping_method' field as a StringField
    shipping_method = StringField(
        'Shipping Method',  # Label for the field
        validators=[
            DataRequired("Shipping method is required"),  # Ensure the field is not empty
            AnyOf(
                values=["Standard", "Express", "Overnight"],  # Predefined valid options
                message="Must be a valid value from pre-defined options: Standard, Express, Overnight."  # Error message if the value is not in the predefined options
            )
        ]
    )

    # Define the 'insurance' field as a BooleanField
    insurance = BooleanField(
        'Insurance',  # Label for the field
        validators=[
            DataRequired("Must be a boolean value")  # Ensure the field is not empty and contains a valid boolean value (True/False)
        ]
    )

    # Define a custom validator to check if the declared value is positive when insurance is selected
    def validate_declared_value(form, field):
        if form.insurance.data:  # Check if the 'insurance' field is selected (True)
            if field.data is None or field.data <= 0:  # Validate that the 'declared_value' is positive
                raise ValidationError("Declared value must be a positive number if Insurance is selected.")
    # Define the 'declared_value' field as an IntegerField
    declared_value = IntegerField(
        'Declared Value',  # Label for the field
        validators=[
            Optional(),  # Allow the field to be empty if insurance is not selected
            validate_declared_value  # Apply the custom validator to check the condition
        ]
    )

    # Define the 'special_instructions' field as a StringField
    special_instructions = StringField(
        'Special Instructions',  # Label for the field
        validators=[
            Optional(),  # Make the field optional; it can be left empty
            Length(max=200, message="Must have a maximum of 200 characters")  # Ensure the input text does not exceed 200 characters
        ]
    )

    # Define the 'bill_of_lading' field as a SelectField
    bill_of_lading = SelectField(
        'Bill of Lading (BL)',  # Label for the field
        choices=[  # Predefined valid options
            ('Master BL', 'Master BL'),
            ('House of BL', 'House of BL'),
            ('Negotiable BL', 'Negotiable BL')
        ],
        validators=[
            DataRequired(message="This field is required."),  # Ensure the field is not empty
            AnyOf(
                ['Master BL', 'House of BL', 'Negotiable BL'],  # Valid options for the field
                message="Must be a valid BL type: Master BL, House of BL, or Negotiable BL."  # Error message if the input does not match the predefined options
            )
        ]
    )
    
    # Custom validator function to check if the address format is valid
    def validate_address(form, field):
        # In this example, the validation logic checks if the address is not just numbers.
        # You can customize this to use regex or other logic to enforce a specific address format.
        if field.data.isdigit():
            # If the data is only digits, raise a ValidationError with a custom message
            raise ValidationError("Please enter a valid address format.")
    # Define the 'carting_point' field as a StringField (text input)
    carting_point = StringField(
        'Carting Point',  # The label for the field
        validators=[  # A list of validators to apply to this field
            DataRequired(message="Carting Point is required"),  # Ensures the field is not left empty
            validate_address  # Applies the custom address validation logic
        ]
    )
    
    # Define the 'cbm' field as a StringField (text input)
    cbm = StringField(
        'CBM',  # The label for the field
        validators=[  # A list of validators to apply to this field
            DataRequired(message="CBM is required"),  # Ensures the field is not left empty
            validate_positive_number  # Applies the custom positive number validation logic
        ]
    )

    # Define the 'cha' field as a SelectField with choices
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
            ),
            Length(max=200, message="Must have a maximum of 200 characters"),  # Ensures the field value doesn't exceed 200 characters
            Regexp(  # Regex to ensure the value is alphanumeric and can include spaces
                regex=r'^[a-zA-Z0-9 ]+$',
                message="CHA must be alphanumeric (letters, numbers, and spaces only)."
            )
        ]
    )
           
    # Predefined choices for the SelectField
    predefined_choices = [
        ('Port of New York', 'Port of New York'),
        ('Los Angeles International Airport', 'Los Angeles International Airport'),
        ('Singapore Customs Office', 'Singapore Customs Office')
    ]
    # Define the 'clearance_place' field as a SelectField with choices
    clearance_place = SelectField(
        'Clearance Place',
        choices=predefined_choices,
        validators=[
            DataRequired(message="This field is required."),
            AnyOf([choice[0] for choice in predefined_choices], message="Must be a valid Clearance Place"),
            Length(max=200, message="Must have a maximum of 200 characters")
        ]
    )  
    # Define a 'custom_clearance_place' field for manual entry
    custom_clearance_place = StringField(
        'Custom Clearance Place',
        validators=[
            Length(max=200, message="Must have a maximum of 200 characters"),
            Regexp(r'^[a-zA-Z0-9 ]+$', message="Must be alphanumeric (letters, numbers, and spaces only).")
        ]
    )
    # Optional: Add validation to ensure either one of the fields is filled
    def validate(self):
        # First, run the default validation
        rv = FlaskForm.validate(self)
        if not rv:
            return False     
        # Ensure that either a predefined or a custom value is provided
        if not self.clearance_place.data and not self.custom_clearance_place.data:
            self.clearance_place.errors.append('You must select or enter a Clearance Place.')
            return False
        # If a custom value is provided, ensure the predefined field is not selected
        if self.custom_clearance_place.data:
            self.clearance_place.data = None
        return True
    
    # Co-Loader Field
    co_loader = StringField('Co-Loader',validators=[DataRequired("Co-Loader is required")])
    
    # Container Stuffing
    container_stuffing = StringField('Co-Loader',validators=[DataRequired("Co-Loader is required")])
    
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

    # gross_weight= IntegerField('Gross Weight', validators=[DataRequired("gross_weight is required")])

    # invoice_currency = StringField('Invoice Currency', validators=[DataRequired("invoice_currency is required")])

    # invoice_currency_value = StringField('Invoice Currency Value', validators=[DataRequired("invoice_currency_value is required")])

    # invoice_date= StringField('Invoice Date', validators=[DataRequired("invoice_date is required")])

    # invoice_number= StringField('Invoice Number', validators=[DataRequired("invoice_number is required")])

    # invoice_type= StringField('Invoice Type', validators=[DataRequired("invoice_type is required")])

    # item_description = StringField('Item Description', validators=[DataRequired("item_description is required")])

    # job_date = StringField('Job Date', validators=[DataRequired("job_date is required")])

    # job_number = StringField('Job Number', validators=[DataRequired("job_number is required")])

    # job_type = StringField('Job Type', validators=[DataRequired("job_type is required")])

    # nature_of_contract = StringField('Nature of Contract', validators=[DataRequired("nature_of_contract is required")])

    # nature_of_payment = StringField('Nature of Payment', validators=[DataRequired("nature_of_payment is required")])

    # net_weight = StringField('Net Weight', validators=[DataRequired("net_weight is required")])

    # number_of_packages = StringField('Number_of_Packages', validators=[DataRequired("number_of_packages is required")])

    # operation_handle_by = StringField('Operation Handle By', validators=[DataRequired("operation_handle_by is required")])

    # plan_date = StringField('Plan Date', validators=[DataRequired("plan_date is required")])

    # pod = StringField('POD', validators=[DataRequired("pod is required")])

    # pol = StringField('POL', validators=[DataRequired("pol is required")])

    # por = StringField('POR', validators=[DataRequired("por is required")])

    # remarks = StringField('Remarks', validators=[DataRequired("remarks is required")])

    # sales_person_name = StringField('Sales Person Name', validators=[DataRequired("sales_person_name is required")])

    # sb_number = StringField('SB Number', validators=[DataRequired("sb_number is required")])

    # sb_number_date = StringField('SB Number Date', validators=[DataRequired("sb_number_date is required")])

    # select_job = StringField('Select Job', validators=[DataRequired("select_job is required")])

    # series = StringField('Series', validators=[DataRequired("series is required")])

    # shipper_or_exporter = StringField('Shipper/Exporter', validators=[DataRequired("shipper_or_exporter is required")])

    # shipping_line = StringField('Shipping Line', validators=[DataRequired("shipping_line is required")])

    # type_of_shipment = StringField('Type of Shipment', validators=[DataRequired("type_of_shipment is required")])

    # unit = StringField('Unit', validators=[DataRequired("unit is required")])

    # unit_type = StringField('Unit Type', validators=[DataRequired("unit_type is required")])
    submit = SubmitField('Next')
