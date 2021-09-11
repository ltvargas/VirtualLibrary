import requests


def get_request(url):
    response = requests.get(url)
    return response.json()

def post_request(url,data):
    response = requests.post(url,data=data)
    return response.json()