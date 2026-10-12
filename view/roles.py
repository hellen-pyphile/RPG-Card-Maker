import requests

class role_model():
    def character_class():
        class_url = 'https://pf2etools.com/classes'
        
        category = input(f"Enter {__name__}'s class: ").strip().lower()
        
        if not category:
            input("The class does not exists.")
            return