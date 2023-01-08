from game import Game, Player


def main() -> None:
    player = Player('Tomer', 'Shafir')
    game = Game(player)

    game.attack().win_or_loose()


main()
