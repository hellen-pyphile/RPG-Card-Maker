import requests
from view.utilities import clean_screen
        
class identity():
    def character_name():
        clean_screen()
        while True:    
            name = input("Enter character's name: ")
            
            if not name.strip():
                print("You must enter the name of the character.")
                continue
            return name
        
    def character_height():
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
        while True:
            personality = input(f"Describe {__name__} personality and motivations:\n")
            
            if not personality.strip():
                print("You can't skip this step!")
                continue
            return personality
    
    def character_past():
        while True:
            past = input(f"{__name__}'s past:\n")
            
            if not past:
                print("You can't skip this step!")
                continue
            return past
            
        
#class attributes():
    
#class habilities():
