import json
from controllers.requests_api import get_request, post_request
from resources.format_text import *
from views.pages.borrow_books import do_borrow_book


select=''
catalog = []


def confirm_borrow(book):
    in_confirm=input("Confirm borrow? y/n: ").lower()
    if in_confirm=='y':
        do_borrow_book(book)
        return_menu()
    elif in_confirm=='n':
        unreserver_book(book)
    else:
        print (form_error+"Error!,the option is wrong"+form_normal)
        confirm_borrow(book)

def unreserver_book(book):
    select_code=book["code"]
    print(form_process+"Unresever book..."+form_normal)
    requests = post_request('http://localhost:8000/unreserver_book/',json.dumps({"code":select_code}))
    return_menu()


def reserver_book(book):
    select_code=book["code"]
    print(form_process+"Resever book..."+form_normal)
    requests = post_request('http://localhost:8000/reserver_book/',json.dumps({"code":select_code}))
    confirm_borrow(requests)


def validation_select():
    global select,catalog
    try:
        select = int(select)
        if  select <= len(catalog) and  select > 0:
            reserver_book(catalog[select-1])
        else:
            print (form_error+"Error!,the option is not found"+form_normal)
            select = input("Choose a book: ")
            validation_select()
    except ValueError:
        print (form_error+"Error!,the number must be integer"+form_normal)
        select = input("Choose a book: ")
        validation_select()
    

def select_book():
    global select
    select=input("Choose a book: ")
    validation_select()
   

def question_borrow():
    in_confirm=input("Do you want to borrow a book? y/n: ").lower()
    if in_confirm=='y':
        select_book()
    elif in_confirm=='n':
        return_menu()
    else:
        print (form_error+"Error!,the option is wrong"+form_normal)
        question_borrow()


def see_catalog():
    print("Loading...")
    global catalog
    catalog = get_request('http://localhost:8000/load_books/')
    cont=1
    if len(catalog)==0:
        print(form_emty+"the library has burned all its books! come back later."+form_normal)
        return True
    for book in catalog:
        print("%d. code: %s title: %s author: %s amount: %s"%(cont,book['code'],book['title'],book['author'],book['amount']))
        cont=cont+1
    question_borrow()
    

def return_menu():
    in_confirm=input("Back to the menu? y/n: ").lower()
    if in_confirm=='y':
        return True
    elif in_confirm=='n':
       see_catalog()
    else:
        print (form_error+"Error!,the option is wrong"+form_normal)
        return_menu()


def avaible_book():
    print(form_title+"Avaible book"+form_normal)
    see_catalog()