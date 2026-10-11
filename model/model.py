import json
import requests
import os

DATASET = "card.json"

def load_character():
    if os.path.exists(DATASET):
        with open(DATASET, "r", encoding='UTF-8') as f:
                    try:    
                        return json.load(f)
                    except json.JSONDecodeError:
                        return []
    return[]

def save_character(character):
    with open(DATASET, "w", encoding='UTF-8') as f:
            json.dump(character, f, indent=4, ensure_ascii=False)
    
