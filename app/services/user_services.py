from app.models.user import User
from werkzeug.security import generate_password_hash

def create_user(username, password, role):
    user = User.find_by_username(username)
    if user:
        return None  # User already exists
    password_hash = generate_password_hash(password)
    user = User(user_id=username, username=username, password_hash=password_hash, role=role)
    user.save_to_db()
    return user
