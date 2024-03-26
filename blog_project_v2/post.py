import requests
from datetime import datetime

class Post:
    def __init__(self):
        self.posts = []

    def request_posts(self):
        response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
        self.posts = response.json()
        for post in self.posts:
            post["time"] = datetime.now().strftime("%B %d, %Y")
            post["author"] = "anonim"

    def get_posts(self):
        return self.posts