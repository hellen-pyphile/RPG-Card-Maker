import requests
from view.utilities import clean_screen
        
class identity():
    def character_name():
        clean_screen()
        name = input("Enter character's name: ")
        
        if name is None:
            try:
                print("You must enter the name of the character.")
            except:
                pass
        
    def character_appearence():
        height = input("Height: ", float)
        
        if height is not float or None: 
            try:
                print("Invalid entry. Try again!")
            except:
                pass
            
    def character_personality():
        personality = input(f"Describe {__name__} personality and motivations:\n")
        
        if personality is None:
            try:
                print("You can't skip this step!")
            except:
                pass
    
    def character_past():
        past = input(f"{__name__}'s past:\n")
        
        if past is None:
            try:
                print("You can't skip this step!")
            except:
                pass
            
        
#class attributes():
    
#class habilities():
