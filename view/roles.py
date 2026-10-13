import requests

class role_model():
    def character_class(character_name: str) -> str:    
        class_url = 'https://pf2etools.com/classes'
            
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
        
        except ValueError:
            print("Error: the URL did not return a valid JSON.")
            return ""
        
        while True:
            category = input(f"Enter {character_name}'s class: ").strip().lower()
            
            if not category:
                print("Give you character a class!")
                continue
            
            if category in available_classes:
                print(f"Cass {category.title()} selected successfully!")
                return category.title()
            else:
                print("Class does not exit. You can try again!")

    def character_archetypes(character_name: str):
        archetype_url = 'https://pf2etools.com/archetypes'
        
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
        
        except ValueError:
            print("Error: The URL did not return a valid JSON.")
            return ""
        
        while True:
            archetype = input(f"What's {character_name}'s archetype?").strip().lower()
                    
            if not archetype:
                print("Enter a archetype!")
                continue
            if archetype in available_archetype:
                print(f"Archetype {archetype.title()} selected successfully!")
                return archetype.title()
            else:
                print("The archetype does not exist. You can try again!")
        
#class attributes():

#class habilities():