import json


class Book:
    def __init__(self,code,title,author,amount):
        self.code=code
        self.title=title
        self.author=author
        self.amount=amount

    def to_json(self):
        return json.dumps({"code":self.code,
        "title":self.title,
        "author":self.author,
        "amount":self.amount})