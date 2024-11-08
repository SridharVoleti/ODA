from flask_login import UserMixin
from app.services.user_services import register_user, login_user, validate_token, get_user

class User(UserMixin):
    def __init__(self, access_token, _id, firstname, lastname, address, phone, username, role, CreatedAt, middlename=None, UpdatedAt=None):
        self.access_token = access_token
        self._id = _id 
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.phone = phone
        self.username = username
        self.role = role
        self.CreatedAt = CreatedAt
        self.UpdatedAt = UpdatedAt

    @property
    def is_authenticated(self):
        """Determines if the user is authenticated based on a valid access token."""
        return self.access_token and validate_token(self.access_token)

    @property
    def is_active(self):
        """Determines if the user account is active."""
        return True

    @property
    def is_anonymous(self):
        """Determines if the user is anonymous (not authenticated)."""
        return not self.is_authenticated

    @staticmethod
    def login(username: str, password: str):
        """Attempts to log in a user and return a User instance or None if login fails."""
        try:
            response = login_user(username, password)
            if response and 'user' in response and 'access_token' in response:
                user_data = response['user']
                user_data['access_token'] = response['access_token']
                return User(**user_data)
            return None
        except Exception as e:
            print(f"Login error: {e}", flush=True)
            return None

    @staticmethod
    def get_user(_id):
        """Retrieves a user by ID and returns a User instance or None if retrieval fails."""
        try:
            data = get_user(_id)
            return User(**data) if data else None
        except Exception as e:
            print(f"Get user error: {e}", flush=True)
            return None
        
    @staticmethod
    def register(user):
        """Registers a new user and returns the result or error."""
        try:
            return register_user(user)
        except Exception as e:
            print(f"Register error: {e}", flush=True)
            return e

    def get_id(self):
        """Returns the user’s unique ID as a string for Flask-Login."""
        return str(self._id)
