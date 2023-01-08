from game.schemas.superhero import SuperHero


class SuperHeroModel:
    def __init__(self) -> None:
        self.all: list[SuperHero] = self._get_all_superheroes()

    def __str__(self) -> str:
        name: list[str] = []
        for superhero in self.all:
            name.append(superhero.name)

        return f"{name}"

    def _get_all_superheroes(self) -> list[SuperHero]:
        ironman = SuperHero('Ironman', 250, 1000)
        blackwidow = SuperHero('Blackwidow', 180, 800)
        spiderman = SuperHero('Spiderman', 190, 700)
        hulk = SuperHero('Hulk', 300, 1100)
        return [ironman, blackwidow, spiderman, hulk]

    def get_superhero(self, index: int) -> SuperHero | None:
        if index < len(self.all) and index >= 0:
            return self.all[index]
        return None
