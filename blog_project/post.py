import requests


class Post:
    def __init__(self):
        self.posts = []

    def request_posts(self):
        response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
        self.posts = response.json()

    def get_posts(self):
        return self.posts