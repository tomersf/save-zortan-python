from .character import Character
from .character_type import CharacterType


class SuperHero(Character):
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.SUPERHERO

    def __str__(self) -> str:
        return 'SuperHero => ' + super().__str__()
