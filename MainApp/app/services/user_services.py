import os
import requests
import json

url = os.getenv("AUTH_URL")
def register_user(user):
    try:
        response = requests.post(url+"/register",json=user)
        print(response.json(),flush=True)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Registration failed...Please Try Again")
    except Exception as e:
        return e
    
def login_user(username:str,password:str):
    try:
        response = requests.post(url+"/login",json={"username":username,"password":password})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Login failed...Please Try Again")
    except Exception as e:
        return e

def get_user(user_id:str):
    try:
        response =  requests.get(f"{url}/get-user/{user_id}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("User not found")
    except Exception as e:
        return e

def validate_token(token:str):
    try:
        response = requests.post(url+"/validate-token",json={"token":token})
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return e