from model.user import User
import json

class Post:
    def __init__(self, id: int, body: str, author: User):
        self.id = id
        self.body = body
        self.author = author