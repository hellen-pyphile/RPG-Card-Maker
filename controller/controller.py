import requests
import os

from IPython.display import clear_output

class_url = 'https://pf2api.com/api/classes/](https://pf2api.com/api/classes/'

def clean_screen():
    if clear_output is not None:
        try:
            clear_output(wait=True)
        except ImportError:
            pass
    os.system('cls' if os.name == 'nt' else 'clear')
    
def character_name():
    clean_screen()
    
    name = input("Enter character name: ")
    
def select_class():
    clean_screen()
    
        
def character_description():
    
