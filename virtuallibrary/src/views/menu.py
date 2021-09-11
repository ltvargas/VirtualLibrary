from views.pages.addbook import add_book
from views.pages.available_books import avaible_book
from views.pages.history_borrow import history_borrow
from views.pages.return_book import return_book
from views.pages.search_book import search_book
from views.login import logout
from resources.format_text import *
import structure.class_user as user


menu_admin=["Add book","Search book","Logout"]
menu_student=["See catalog","Return book","Borrow history","Logout"]


def show_option_student(option):
    if option == "1":
        avaible_book()
        asing_menu()
    elif option == "2":
        return_book()
        asing_menu()
    elif option == "3":
        history_borrow()
        asing_menu()
    else:
        logout()


def show_option_admin(option):
    if option == "1":
        add_book()
        asing_menu()
    elif option == "2":
        search_book()
        asing_menu()
    else:
        logout()


def validation_option_student(option):
    if option!='1' and option!='2' and option!='3' and option!='4':
        print(form_error+"Error, this option does not exist"+form_normal)
        in_option()
    else:
        show_option_student(option)


def validation_option_admin(option):
    if option!='1' and option!='2' and option!='3':
        print(form_error+"Error, this option does not exist"+form_normal)
        in_option()
    else:
        show_option_admin(option)


def in_option():
    option = input("\n"+"Choose an option: ")
    if user.session.rol=='admin':
        validation_option_admin(option)
    else:
        validation_option_student(option)


def show_menu(menu):
    print(form_title+"Menu"+form_normal)
    cont=1
    for item in menu:
        print("%d. %s"%(cont,item))
        cont=cont+1
    in_option()


def asing_menu():
    if user.session.rol=='admin':
        show_menu(menu_admin)
    else:
        show_menu(menu_student)

