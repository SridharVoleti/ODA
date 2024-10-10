import random
import string
from datetime import datetime

def generate_invoice_number():
    # Generate a random 6-digit number
    random_digits = f"{random.randint(0, 999999):06}"
    
    # Generate a random 3-letter uppercase string
    random_letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    
    # Generate a random digit at the end
    random_end_digit = random.randint(0, 9)
    
    # Combine all parts into the desired format
    unique_id = f"INV-{random_digits}-{random_letters}-{random_end_digit}"
    
    return unique_id

def generate_job_id():
    # Generate a random 5-digit number
    random_digits = f"{random.randint(0, 99999):05}"
    
    # Combine with the "JOB" prefix
    job_id = f"JOB{random_digits}"
    
    return job_id

def generate_sb_id():
    # Generate a random 8-digit number
    random_digits = f"{random.randint(0, 99999999):08}"
    
    # Combine with the "SB" prefix
    sb_id = f"SB{random_digits}"
    
    return sb_id

def generate_shipment_id() -> str:
    """
    Generate a unique ID in the format SHIPMENTYYYYMMDDHHMMSS, using the current date and time.
    """
    current_time = datetime.now()
    # Format the time as YYYYMMDDHHMMSS (year, month, day, hour, minute, second)
    time_str = current_time.strftime("%Y%m%d%H%M%S")
    return f"SHIPMENT{time_str}"
def generate_container_id() -> str:
    """
    Generate a unique ID in the format SHIPMENTYYYYMMDDHHMMSS, using the current date and time.
    """
    current_time = datetime.now()
    # Format the time as YYYYMMDDHHMMSS (year, month, day, hour, minute, second)
    time_str = current_time.strftime("%Y%m%d%H%M%S")
    return f"CONTAINER{time_str}"