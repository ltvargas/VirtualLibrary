import json
import structure.class_user as user
from controllers.requests_api import get_request, post_request
from resources.format_text import *
from datetime import date


select=''
catalog = []


def alert_return(response):
    if response:
        print(form_succes+"Success return book!"+form_normal)
        return_book()
    else:
        print(form_error+"Error!, the book could not be return"+form_normal)
        return_book()
    

def validation_return(borrow):
    borrow_date=borrow["date_issue"]
    now_date =date.today()
    d_now = date(now_date.year,now_date.month,now_date.day)
    split_borrow_date=borrow_date.split('-')
    d_borrow_date = date(int(split_borrow_date[0]),int(split_borrow_date[1]),int(split_borrow_date[2]))
    different=abs(d_borrow_date-d_now).days
    if(different<30):
        do_return_book(borrow)
    else:
        print(form_error+"Error!,You cannot return the book you have passed the 30 days, contact the library manager"+form_normal)
        return_menu()


def do_return_book(borrow):
    select_code=borrow["book"]["code"]
    print(form_process+"Returning book..."+form_normal)
    requests = post_request('http://localhost:8000/return_book/',json.dumps({"code":select_code}))
    print(requests)
    try:
        if requests["date_devolution"]:
            alert_return(True)
    except Exception:
            print (form_error+requests["error"]+form_normal)
            alert_return(False)
            return_menu()
   
  
def return_menu():
    in_confirm= input("Back to the menu? y/n: ").lower()
    if in_confirm=='y':
        return True
    elif in_confirm=='n':
       choose_borrow_return()
    else:
        print (form_error+"Error!,the option is wrong"+form_normal)
        return_menu()


def question_return_menu(borrow):
    in_confirm= input("do you want to return the book? y/n: ").lower()
    if in_confirm=='y':
        validation_return(borrow)
    elif in_confirm=='n':
       return False
    else:
        print (form_error+"Error!,the option is wrong"+form_normal)
        question_return_menu(borrow)


def validation_select():
    global select,catalog
    try:
        select = int(select)
        if  select <= len(catalog) and  select > 0:
            question_return_menu(catalog[select-1])
            
        else:
            print (form_error+"Error!,the option is not found"+form_normal)
            select = input("Choose a book: ")
            validation_select()
    except ValueError:
        print (form_error+"Error!,the number must be integer"+form_normal)
        select = input("Choose a book: ")
        validation_select()


def choose_borrow_return():
    global select
    select=input("Choose a book:")  
    validation_select()


def show_borrow_unreturn():
    print("Loading...")
    global catalog
    catalog = get_request('http://localhost:8000/load_borrow/'+ user.session.user)
    cont=1
    if len(catalog)==0:
        print(form_emty+"you do not have the borrow pending"+form_normal)
        return True
    for borrow in catalog:
        print("%d. Borrow: date_issue: %s date_devolution: %s \nBorrowed book: code: %s title: %s author: %s  \n"%(cont,borrow['date_issue'],borrow['date_devolution'],borrow['book']['code'],borrow['book']['title'],borrow['book']['author']))
        cont=cont+1
    choose_borrow_return()
    

def return_book():
    print(form_title+"Return book"+form_normal)
    show_borrow_unreturn()
