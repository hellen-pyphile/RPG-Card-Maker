from view.identity import identity
from model import Character, load_character, save_character

class new_character:
    @staticmethod
    def create_character():
        name = identity.character_name()
        height = identity.character_height()
        personality = identity.character_personality(name)
        past = identity.character_past(name)

        new_character = Character(
            name = name,
            height = height,
            personality = personality,
            past = past
        )

        data = load_character()
        data.append(new_character.to_dict())
        save_character(data)

        print(f"\nPersonagem '{new_character.name}' salvo com sucesso!")
        return new_character