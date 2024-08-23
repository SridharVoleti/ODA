from wtforms import ValidationError
from datetime import datetime
#  Define a custom validator to check if the input is a positive number
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
    
    # Define a custom validator to check if the date is in the future
def validate_future_date(form, field):
    if field.data <= datetime.today().date():  # Check if the date is today or in the past
        raise ValidationError("Delivery date must be in the future.")  # Raise an error if the date is not in the future
# Define a custom validator to check if the declared value is positive when insurance is selected
def validate_declared_value(form, field):
    if form.insurance.data:  # Check if the 'insurance' field is selected (True)
        if field.data is None or field.data <= 0:  # Validate that the 'declared_value' is positive
            raise ValidationError("Declared value must be a positive number if Insurance is selected.")