from view.utilities import clean_screen

        
class identity():
    @staticmethod
    def character_name() -> str:
        clean_screen()
        while True:    
            name = input("Enter character's name: ")
            
            if not name.strip():
                print("You must enter the name of the character.")
                continue
            return name
        
    @staticmethod
    def character_height() -> float:
            while True:
                try:
                    height = float(input("Height: "))
                    if height <= 0:
                        print("Height must be greater than 0.")
                        continue
                    return height
                except ValueError:
                    print("Invalid entry. Try again!")
         
    @staticmethod       
    def character_personality(character_name: str) -> str:
        while True:
            personality = input(f"Describe {character_name} personality and motivations:\n").strip()
            
            if not personality.strip():
                print("You can't skip this step!")
                continue
            return personality
    
    @staticmethod
    def character_past(character_name: str) -> str:
        while True:
            past = input(f"{character_name}'s past:\n").strip()
            
            if not past:
                print("You can't skip this step!")
                continue
            return past
            
        
#class attributes():
    
#class habilities():
