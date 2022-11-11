from score import Scoreboard
from handle_input import get_input, check_name
from custom_exceptions import PlayerExistsError


class Player:

    def __init__(self, name: str):
        self._name = name
        self._scoreboard: Scoreboard = Scoreboard(self)

    def __repr__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def scoreboard(self):
        return self._scoreboard


class PlayerDB:

    _players = []

    @classmethod
    def add(cls, player: Player):
        if player not in cls._players:
            cls._players.append(player)
        else:
            raise PlayerExistsError(f'{player} already exists')

    @classmethod
    def players(cls):
        return cls._players


def create_player():
    try:
        player_name = get_input('Enter your name: ', check_name)
    except ValueError:
        raise ValueError
    else:
        new_player = Player(player_name.title())
        return new_player
