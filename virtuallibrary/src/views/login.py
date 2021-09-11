import structure.class_user as requests_user
import pandas as pd
from resources.format_text import *


def login(user,rol):
    print("\n"+form_succes+"Successful login!"+form_normal)
    requests_user.session=requests_user.Session(user,rol)
    print("Hi! %s"%requests_user.session.user)
    return True
  

def logout():
    print("Bye! %s"%requests_user.session.user)
    print("\n"+form_succes+"Successful logout!"+form_normal)
    requests_user.session.user=''
    requests_user.session.rol=''
    exit()


def error_credentials():
    response=input("Try again y/n: ").lower()
    if response =='y':
        return in_credentials()   
    elif  response =='n':
        return False
    else:
        print (form_error+"Error!,the option is wrong"+form_normal)
        return error_credentials()


def verify_credentials(user,password):
    credentials = pd.read_csv("credentials.csv")
    request=credentials.loc[credentials.email==user]
    request=request.reset_index()
    if len(request)==0:
        print(form_error+"Error!, incorrect credentials"+form_normal)
        return error_credentials()
    else:
        if request.password[0]==password:
            return login(user,request.rol[0])
        else:
            print(form_error+"Error!, incorrect credentials"+form_normal)
            return error_credentials()


def in_credentials():
    user = input("Enter user: ")
    password = input("Enter Password: ")
    return verify_credentials(user,password)
    