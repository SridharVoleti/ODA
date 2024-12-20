from flask_login import UserMixin
import requests
import os

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
        try:
            response =requests.post(f"{os.getenv("AUTH_URL")}/validate-token",json={"token":self.access_token})
            return response.status_code == 200
        except Exception as e:
            print(f"is_authenticated error: {str(e)}")
        
    @property
    def is_active(self):
        """Determines if the user account is active."""
        return True

    @property
    def is_anonymous(self):
        """Determines if the user is anonymous (not authenticated)."""
        return not self.is_authenticated

    def get_id(self):
        """Returns the user’s unique ID as a string for Flask-Login."""
        return str(self._id)
