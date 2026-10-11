import requests
from view.utilities import clean_screen
        
class identity():
    def character_name():
        clean_screen()
        name = input("Enter character's name: ")
        
        if not name.strip():
            try:
                print("You must enter the name of the character.")
            except:
                pass
        
    def character_appearence():
            while True:
                try:
                    height = float(input("Height: "))
                    if height <= 0:
                        print("Height must be greater than 0.")
                        continue
                    return height
                except ValueError:
                    print("Invalid entry. Try again!")
                
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
