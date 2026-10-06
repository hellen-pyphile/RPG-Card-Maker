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
    