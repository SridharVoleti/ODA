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
    """
    Validates that the given field contains a date that is in the future.
    The field should already be a datetime object.
    """  
    # Compare the field's date with the current date
    # if field.data.date() <= datetime.now().date():
    #     raise ValidationError("The date must be in the future.")
    pass

