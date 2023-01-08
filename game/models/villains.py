from game.schemas.villain import Villain


class VillainModel:
    def __init__(self) -> None:
        self.all: list[Villain] = self._get_all_villains()

    def __str__(self) -> str:
        name: list[str] = []
        for villain in self.all:
            name.append(villain.name)

        return f"{name}"

    def get_villain(self, index: int) -> Villain | None:
        if index < len(self.all) and index >= 0:
            return self.all[index]
        return None

    def _get_all_villains(self) -> list[Villain]:
        thanos = Villain('Thanos', 400, 1500)
        redskull = Villain('Redskull', 300, 800)
        proxima = Villain('Proxima', 320, 800)
        return [thanos, redskull, proxima]
