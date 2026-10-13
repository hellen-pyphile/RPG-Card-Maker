import requests
#from view.identity import character?

class role_model():
    def character_class(character_name: str) -> str:    
        class_url = 'https://pf2etools.com/classes'
        
        while True:
            category = input(f"Enter {character_name}'s class: ").strip().lower()
            
            if not category:
                input("Give you character a class!")
                continue
            
            try:
                class_response = requests.get(class_url)
                class_response.raise_for_status()
                
                data = class_response.json()
                
                available_classes = [c['name'].lower() for c in data.get('results', [])]
            
                if category in available_classes:
                    print(f"Class {category.capitalize()} selected successfully!")
                    return category.capitalize()
                else:
                    print("The class does not exist. You can try again!")
                    
            except requests.exceptions.RequestException as e:
                print(f"Error connecting to the API: {e}")
                return ""
            
        
    def character_archetypes():
        archetype_url = 'https://pf2etools.com/archetypes'
        
        archetype = input("")
        
#class attributes():

#class habilities():