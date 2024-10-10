import requests
from app.models.container import Container

def get_containers():
    url = "http://127.0.0.1:5000/api/containers"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

def create_container(container : "Container"):
    url = "http://127.0.0.1:5000/api/container"
    response = requests.post(url,json=container)
    if response.status_code == 201:
        return response.json()

def create_containers(containers):
    url = "http://127.0.0.1:5000/api/containers"
    response = requests.post(url,json=containers)
    if response.status_code == 201:
        return response.json()