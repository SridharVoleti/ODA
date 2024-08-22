# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,DateField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Regexp,NumberRange,Optional,AnyOf

class BookingForm(FlaskForm):
    """
    Form for creating a new booking with validation.
    """
    shipment_id = IntegerField('Shipment ID', validators=[DataRequired("shipment_id is required"),Regexp("Must be alpha_numeric")])
    shipping_company = IntegerField('shipping company ID', validators=[DataRequired("shipping_company is required"),Length("Must have maximum of 200 characters"),Regexp("Must be alpha_numeric")])
    sender_name = StringField('Sender Name', validators=[DataRequired("sender_name is required"),Length("Must have maximum of 50 characters"),Regexp("Must be alpha_numeric")])
    sender_address = StringField('Sender Address', validators=[DataRequired("sender_address is required"),])
    consignee = StringField('Consignee', validators=[DataRequired("consignee is required"),Length("Must have maximum of 200 characters"),Regexp("Must be alpha_numeric")])
    consignee_address = StringField('Consignee Address', validators=[DataRequired("consignee_address is required")])
    package_type = SelectField('Package Type',choices=[
            ('Option1', 'Option1'),
            ('Option2', 'Option2'),
            ('Option3', 'Option3')
        ], validators=[DataRequired("package_type is required"),AnyOf(['Option1', 'Option2', 'Option3'], message="Must be a valid Package Type.")])
    weight = IntegerField('Weight', validators=[DataRequired("weight is required"),NumberRange("Weight must be within the allowed carrier range")])
    dimensions = StringField('Dimensions', validators=[DataRequired("dimensions is required"),])
    shipping_date = DateField('Shipping Date', validators=[DataRequired("Must be a valid date")])
    delivery_date = DateField('Delivery Date', validators=[DataRequired("Must be a valid date")])
    shipping_method = StringField('Shipping Method', validators=[DataRequired("shipping_method is required")])
    insurance = BooleanField('Insurance', validators=[DataRequired("Must be a boolean value")])
    declared_value = IntegerField('Declared Value', validators=[DataRequired("Must be a positive number if Insurance is selected")])
    special_instructions = StringField('Special Instructions', validators=[Optional("This is optional field"),Length("Must have maximum of 200 characters")])
    bill_of_lading = SelectField('Bill of Lading (BL)',
        choices=[
            ('Master BL', 'Master BL'),
            ('House of BL', 'House of BL'),
            ('Negotiable BL', 'Negotiable BL')
        ],
        validators=[
            DataRequired(message="This field is required."),
            AnyOf(['Master BL', 'House of BL', 'Negotiable BL'], message="Must be a valid BL type.")
        ])
    carting_point = StringField('Carting Point', validators=[DataRequired("carting_point is required"),])
    cbm = StringField('CBM', validators=[DataRequired("cbm is required")])
    cha = SelectField('CHA',choices=[
            ('ABC Customs Services Ltd', 'ABC Customs Services Ltd'),
            ('Global Trade Brokers Inc', 'Global Trade Brokers Inc'),
            ('XYZ Logistics and Customs', 'XYZ Logistics and Customs')],validators=[
            DataRequired(message="This field is required."),
            AnyOf(['ABC Customs Services Ltd', 'Global Trade Brokers Inc', 'XYZ Logistics and Customs'], message="PrePopulate through a configuration page set to save time."),Length("Must have maximum of 200 characters"),Regexp("Must be alpha_numeric")
        ])         
    clearance_place = StringField('Clearance Place', validators=[DataRequired("clearance_place is required")])
    co_loader = StringField('Co-Loader', validators=[DataRequired("co_loader is required")])
    container_stuffing = StringField('Container Stuffing', validators=[DataRequired("container_stuffing is required")])
    file_reference_number = StringField('File Reference Number', validators=[DataRequired("file_reference_number is required")])
    forwarder = StringField('Forwarder', validators=[DataRequired("forwarder is required")])
    fpod = StringField('FPOD', validators=[DataRequired("fpod is required")])
    gross_weight= StringField('Gross Weight', validators=[DataRequired("gross_weight is required")])
    invoice_currency = StringField('Invoice Currency', validators=[DataRequired("invoice_currency is required")])
    invoice_currency_value = StringField('Invoice Currency Value', validators=[DataRequired("invoice_currency_value is required")])
    invoice_date= StringField('Invoice Date', validators=[DataRequired("invoice_date is required")])
    invoice_number= StringField('Invoice Number', validators=[DataRequired("invoice_number is required")])
    invoice_type= StringField('Invoice Type', validators=[DataRequired("invoice_type is required")])
    item_description = StringField('Item Description', validators=[DataRequired("item_description is required")])
    job_date = StringField('Job Date', validators=[DataRequired("job_date is required")])
    job_number = StringField('Job Number', validators=[DataRequired("job_number is required")])
    job_type = StringField('Job Type', validators=[DataRequired("job_type is required")])
    nature_of_contract = StringField('Nature of Contract', validators=[DataRequired("nature_of_contract is required")])
    nature_of_payment = StringField('Nature of Payment', validators=[DataRequired("nature_of_payment is required")])
    net_weight = StringField('Net Weight', validators=[DataRequired("net_weight is required")])
    number_of_packages = StringField('Number_of_Packages', validators=[DataRequired("number_of_packages is required")])
    operation_handle_by = StringField('Operation Handle By', validators=[DataRequired("operation_handle_by is required")])
    plan_date = StringField('Plan Date', validators=[DataRequired("plan_date is required")])
    pod = StringField('POD', validators=[DataRequired("pod is required")])
    pol = StringField('POL', validators=[DataRequired("pol is required")])
    por = StringField('POR', validators=[DataRequired("por is required")])
    remarks = StringField('Remarks', validators=[DataRequired("remarks is required")])
    sales_person_name = StringField('Sales Person Name', validators=[DataRequired("sales_person_name is required")])
    sb_number = StringField('SB Number', validators=[DataRequired("sb_number is required")])
    sb_number_date = StringField('SB Number Date', validators=[DataRequired("sb_number_date is required")])
    select_job = StringField('Select Job', validators=[DataRequired("select_job is required")])
    series = StringField('Series', validators=[DataRequired("series is required")])
    shipper_or_exporter = StringField('Shipper/Exporter', validators=[DataRequired("shipper_or_exporter is required")])
    shipping_line = StringField('Shipping Line', validators=[DataRequired("shipping_line is required")])
    type_of_shipment = StringField('Type of Shipment', validators=[DataRequired("type_of_shipment is required")])
    unit = StringField('Unit', validators=[DataRequired("unit is required")])
    unit_type = StringField('Unit Type', validators=[DataRequired("unit_type is required")])
    submit = SubmitField('Submit')
