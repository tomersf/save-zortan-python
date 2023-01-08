from __future__ import annotations
from textwrap import dedent
from random import randint
from .schemas.player import Player
from .schemas.game_state import GameState
from .models.superheroes import SuperHeroModel
from .models.villains import VillainModel
from .schemas.superhero import SuperHero
from .schemas.villain import Villain
from .schemas.life import Life
from .constants import LOST_MSG, WIN_MSG, NUM_OF_ATTACKS, START_MSG


class Game:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.state = GameState.INITIALIZING
        self.superheroes = SuperHeroModel()
        self.villains = VillainModel()

    def __repr__(self) -> str:
        return "<class 'Game'>"

    def __str__(self) -> str:
        return dedent(f"""\
                Player: {self.player},
                State: {self.state},
                Superheroes: {self.superheroes},
                Villains: {self.villains}""")

    def attack(self) -> Game:
        self.state = GameState.IN_PROGRESS
        print(START_MSG)
        print('Starting attack...')

        superheroes_len = len(self.superheroes.all)
        villains_len = len(self.villains.all)
        for attack_num in range(NUM_OF_ATTACKS):
            hero_index = randint(0, superheroes_len - 1)
            villain_index = randint(0, villains_len - 1)

            chosen_hero = self.superheroes.get_superhero(hero_index)
            chosen_villain = self.villains.get_villain(villain_index)

            if chosen_hero and chosen_villain:
                self.__do_attack(attack_num, chosen_hero, chosen_villain)
            else:
                print('ERROR! No superhero or villain to fight with')
        return self

    def __do_attack(self, attack_num: int, hero: SuperHero, villain: Villain) -> None:
        Life.increment_hero_life(hero.life)
        Life.increment_villain_life(villain.life)

        print(
            f"Attack: {attack_num + 1} => {hero.name} is going to fight with {villain.name}")
        Life.decrement_hero_life(villain.attack_power)
        Life.decrement_villain_life(hero.attack_power)

    def win_or_loose(self) -> Game:
        print('=' * 40)
        if Life.hero_life >= Life.villain_life:
            self.state = GameState.WIN
            print(WIN_MSG)
        else:
            self.state = GameState.LOSE
            print(LOST_MSG)
        return self
