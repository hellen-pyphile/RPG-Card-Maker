import requests
import os

from IPython.display import clear_output

def clean_screen():
    if clear_output is not None:
        try:
            clear_output(wait=True)
        except ImportError:
            pass
    os.system('cls' if os.name == 'nt' else 'clear')
        
class identity():
    def character_name():
        clean_screen()
        
        name = input("Enter character name: ")
        if name is None:
            try:
                print("You must enter the name of the character.")
            except:
                pass
                    
    def character_description():
        description = input("")
    
class role_model():
    def character_class():
        class_url = 'https://pf2etools.com/classes'
        
        category = input(f"Enter {__name__}'s class: ").strip().lower()
        
        if not category:
            input("The class does not exists.")
            return
        
#class attributes():
    
#class habilities():
