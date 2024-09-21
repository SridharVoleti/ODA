from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user, login_required
def role_required(required_role):
    def decorator(func):
        @wraps(func)
        @login_required
        def wrapper(*args, **kwargs):
            if current_user.role != required_role:
                flash('Access denied: insufficient permissions.', 'danger')
                return redirect(url_for('auth.login'))
            return func(*args, **kwargs)
        return wrapper
    return decorator
