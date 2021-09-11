from controllers.requests_api import get_request
from resources.format_text import *


code_book = ''


def show_book(book):
    print("code: %s title: %s author: %s amount: %s"%(book['code'],book['title'],book['author'],book['amount']))
    return_menu()
    return True


def to_search_book(code_book):
    print(form_process+"Research book..."+form_normal)
    requests = get_request('http://localhost:8000/search_books/'+code_book)
    try:
        if requests["code"]:
            show_book(requests)
    except Exception:
        print (form_error+requests["error"]+form_normal)
        return_menu()
   


def input_code_book():
    global code_book
    code_book = input("Enter code:")
    to_search_book(code_book)


def return_menu():
    in_confirm= input("Back to the menu? y/n: ").lower()
    if in_confirm=='y':
        return True
    elif in_confirm=='n':
       input_code_book()
    else:
        print (form_error+"Error!,the option is wrong"+form_normal)
        return_menu()

def search_book():
    print(form_title+"Search book"+form_normal)
    input_code_book()