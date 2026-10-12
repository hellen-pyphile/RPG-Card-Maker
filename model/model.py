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
    
class Character:
    def __init__(self, name: str, height: float, personality: str, past: str):
        if not name or not name.strip():
            raise ValueError("You must name the character.")
        if height <= 0:
            raise ValueError("The height can't be shorter than 0.")

        self.name = name.strip()
        self.height = height
        self.personality = personality.strip()
        self.past = past.strip()

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "height": self.height,
            "personality": self.personality,
            "past": self.past
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            height=data["height"],
            personality=data["personality"],
            past=data["past"]
        )

    def __repr__(self) -> str:
        return f"<Character: {self.name} ({self.height}m)>"