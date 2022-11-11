from score import Scoreboard
from dataclasses import dataclass, field
from handle_input import get_input, check_name
from custom_exceptions import PlayerExistsError


@dataclass(frozen=True)
class Player:

    name: str = field(compare=True)
    scoreboard: Scoreboard = Scoreboard()

    def __repr__(self):
        return self.name


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
