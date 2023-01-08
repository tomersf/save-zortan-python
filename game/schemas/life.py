class Life:
    hero_life = 0
    villain_life = 0

    @staticmethod
    def increment_hero_life(life: int) -> None:
        Life.hero_life += life

    @staticmethod
    def decrement_hero_life(life: int) -> None:
        Life.hero_life -= life

    @staticmethod
    def increment_villain_life(life: int) -> None:
        Life.villain_life += life

    @staticmethod
    def decrement_villain_life(life: int) -> None:
        Life.villain_life -= life
