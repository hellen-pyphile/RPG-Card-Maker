from view.identity import identity
from model.model import character, load_character, save_character

class CharacterController:
    @staticmethod
    def create_character():
        name = identity.character_name()
        height = identity.character_height()
        personality = identity.character_personality(name)
        past = identity.character_past(name)

        new_char = character(
            name=name,
            height=height,
            personality=personality,
            past=past
        )

        data = load_character()
        data.append(new_char.to_dict())
        save_character(data)

        print(f"\n'{new_char.name}' successfully saved!")
        return new_char 