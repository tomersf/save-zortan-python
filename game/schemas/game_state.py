from enum import Enum, auto


class GameState(Enum):

    INITIALIZING = auto()
    IN_PROGRESS = auto()
    WIN = auto()
    LOSE = auto()
