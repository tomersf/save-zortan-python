from .character import Character
from .character_type import CharacterType


class Villain(Character):
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.VILLAIN

    def __str__(self) -> str:
        return 'Villain => ' + super().__str__()
