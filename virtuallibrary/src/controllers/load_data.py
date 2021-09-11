from resources.format_text import *
from resources.data_database import *
from controllers.requests_api import post_request
import structure.class_book as class_book


def load_previus_data():
    print(form_process+"Load previus data...\n"+form_normal)
    for data in data_previus:
        book=class_book.Book(data["code"],data["title"],data["author"],data["amount"])
        data_book=book.to_json()
        requests=post_request('http://localhost:8000/create_book/',data_book)