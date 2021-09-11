from controllers.requests_api import get_request
from resources.format_text import *
import structure.class_user as user


def see_history():
    catalog = get_request('http://localhost:8000/borrow_history/'+ user.session.user)
    if len(catalog)==0:
        print(form_emty+"You have not do any borrow"+form_normal)
        return True
    for borrow in catalog:
        print("Borrow: date_issue: %s date_devolution: %s \nBorrowed book: code: %s title: %s author: %s  \n"%(borrow['date_issue'],borrow['date_devolution'],borrow['book']['code'],borrow['book']['title'],borrow['book']['author']))
    return_menu()
    

def return_menu():
    in_confirm=input("Back to the menu? y/n: ").lower()
    if in_confirm=='y':
        return True
    elif in_confirm=='n':
      see_history()
    else:
        print (form_error+"Error!,the option is wrong"+form_normal)
        return_menu()


def history_borrow():
    print(form_title+"History borrow"+form_normal)
    print("Loading...")
    see_history()
    