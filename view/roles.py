import requests

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
            
        
    def character_archetypes(character_name: str):
        archetype_url = 'https://pf2etools.com/archetypes'
        
        while True:
            archetype = input(f"What's {character_name}'s archetype?")
            
            if not archetype:
                input("Enter a archetype!")
                continue
            
            try:
                archetype_response = requests.get(archetype_url)
                archetype_response.raise_for_status()
                
                data = archetype_response.json()
                                
                available_archetype = [c['name'].lower() for c in data.get('results', [])]
                            
                if archetype in available_archetype:
                    print(f"Class {archetype.capitalize()} selected successfully!")
                    return archetype.capitalize()
                else:
                    print("The archetype does not exist. You can try again!")                        
            except requests.exceptions.RequestException as e:
                print(f"Error connecting to the API: {e}")
                return ""
        
#class attributes():

#class habilities():