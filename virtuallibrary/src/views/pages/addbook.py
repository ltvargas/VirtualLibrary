import structure.class_book as class_book
from controllers.requests_api import post_request
from resources.format_text import *


code_book=''
title_book=''
author_book=''
amount_book=0


def alert_book(response,message):
    if response:
        print(form_succes+"Success %s book!"%message+form_normal)
    else:
        print(form_error+"Error!, the book could not be registered"+form_normal)
    return_menu()


def register_book():
    print (form_process+"registering..."+form_normal)
    book=class_book.Book(code_book,title_book,author_book,amount_book)
    data_book=book.to_json()
    requests=post_request('http://localhost:8000/create_book/',data_book)
    try:
        if requests["code"]:
            alert_book(True,'registered')
    except Exception:
        try:
            if requests["notice"]:
                print (form_error+requests["notice"]+form_normal)
                alert_book(True,'updated')
        except Exception:
            print (form_error+requests["error"]+form_normal)
            alert_book(False)
            return_menu()
 

def return_menu():
    in_confirm=input("Back to the menu? y/n: ").lower()
    if in_confirm=='y':
        return True
    elif in_confirm=='n':
        input_data_book()
    else:
        print (form_error+"Error!,the option is wrong"+form_normal)
        return_menu()


def confirm_register_book():
    in_confirm=input("Confrim y/n: ").lower()
    if in_confirm=='y':
        register_book()
    elif in_confirm=='n':
        return_menu()
    else:
        print (form_error+"Error!,the option is wrong"+form_normal)
        confirm_register_book()


def validation_amount(amount):
    try:
        global amount_book
        amount_book_int = int(amount)
        amount_book=amount_book_int
        return amount_book_int
    except ValueError:
        print (form_error+"Error!,the number must be integer"+form_normal)
        amount = input("Enter amount:")
        validation_amount(amount)


def input_data_book():
    global code_book,title_book,author_book,amount_book
    print("\nData book")
    code_book = input("Enter code:")
    title_book = input("Enter title:")
    author_book = input("Enter author:")
    amount_book = input("Enter amount:")
    validation_amount(amount_book)
    confirm_register_book()


def add_book():
    print(form_title+"Add book"+form_normal)
    input_data_book()
   