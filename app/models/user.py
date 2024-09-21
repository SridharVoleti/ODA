from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, username, password_hash, role):
        self.user_id = user_id  # Assuming user_id is a unique identifier
        self.username = username
        self.password_hash = password_hash
        self.role = role

    @staticmethod
    def find_by_username(username):
        from app import mongo  # Import inside the function to avoid circular import issues
        user_data = mongo.db.users.find_one({"username": username})
        if user_data:
            return User(
                user_id=user_data.get("_id"),  # Use the correct field that identifies the user uniquely
                username=user_data.get("username"),
                password_hash=user_data.get("password_hash"),
                role=user_data.get("role")
            )
        return None

    def save_to_db(self):
        from app import mongo
        mongo.db.users.insert_one({
            "_id": self.user_id,
            "username": self.username,
            "password_hash": self.password_hash,
            "role": self.role
        })

    def get_id(self):
        # Ensure this returns a unique identifier for the user; can be self.user_id, self.username, or another unique field
        return str(self.user_id)  # Make sure it returns a string representation of the ID
