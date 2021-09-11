from controllers.load_data import load_previus_data
from views.login import in_credentials
from resources.format_text import *
from views.menu import asing_menu


def main():
    #do this only once
    #load_previus_data()
    #comment load_previus_data() after run
    print(form_title+"welcome to the virtual library\n"+form_normal)
    if in_credentials():
        asing_menu()
    else:
        print(form_title+"Trank for visit"+form_normal)

   
main()