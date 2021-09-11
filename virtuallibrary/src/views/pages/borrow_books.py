import json
import structure.class_user as user
from controllers.requests_api import post_request
from resources.format_text import *


def unreserver_book(book):
    select_code=book["code"]
    print(form_process+"Unresever book..."+form_normal)
    requests = post_request('http://localhost:8000/unreserver_book/',json.dumps({"code":select_code}))


def alert_borrow(response,book):
    if response:
        print(form_succes+"Success borrow book!"+form_normal)
        return True
    else:
        print(form_error+"Error!, the book could not be borrow"+form_normal)
        unreserver_book(book)
        return False


def do_borrow_book(book):
    print("Borrow book...")
    requests = post_request('http://localhost:8000/borrow_book/',json.dumps({"user_email":user.session.user,"book":book}))
    print(requests)
    try:
        if requests["date_issue"]:
            alert_borrow(True,book)
    except Exception:
            print (form_error+requests["error"]+form_normal)
            alert_borrow(False,book)
  
  
    



   
    
