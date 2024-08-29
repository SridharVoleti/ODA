from wtforms import ValidationError
from datetime import datetime
#  Define a custom validator to check if the input is a positive number
def validate_positive_number(form, field):
    try:
        # Attempt to convert the field's data to a float
        value = field.data
        # Raise a validation error if the value is not positive
        if value <= 0:
            raise ValidationError("Dimensions must be a positive number.")
    except ValueError:
        # Raise a validation error if the conversion to float fails (input is not a number)
        raise ValidationError("Dimensions must be a positive number.")
    
    # Define a custom validator to check if the date is in the future
def validate_future_date(form, field):
    # Convert the string to a datetime.date object
    try:
        date = datetime.strptime(field.data, '%Y-%m-%d').date()  # Adjust format if necessary
    except ValueError:
        raise ValidationError("Invalid date format. Please use YYYY-MM-DD.")
    
    # Check if the date is today or in the past
    if date <= datetime.today().date():
        raise ValidationError("Delivery date must be in the future.")

