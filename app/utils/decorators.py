from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user, login_required
def role_required(required_role:list):
    def decorator(func):
        @wraps(func)
        @login_required
        def wrapper(*args, **kwargs):
            if not current_user.role in required_role:
                return redirect(url_for('error.unauthorised'))
            return func(*args, **kwargs)
        return wrapper
    return decorator
