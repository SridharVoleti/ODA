from flask import request,abort
from flask_jwt_extended import decode_token

def verify_token(required_roles=None):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if not token:
        abort(401, description="Missing token")
    
    decoded_token = decode_token(token)
    user = decoded_token['sub']
    if required_roles and user['role'] not in required_roles:
        abort(403, description="Forbidden: Insufficient privileges")
    return user