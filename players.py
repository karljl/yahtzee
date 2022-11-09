from score import Scoreboard
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Player:

    name: str = field(compare=True)
    scoreboard: Scoreboard = Scoreboard()

    def __repr__(self):
        return self.name


def create_player():
    player_name = input('Enter your name: ').title()
    new_player = Player(player_name)
    return new_player


class PlayerDB:

    _players = []

    @classmethod
    def add(cls, player: Player):
        if player not in cls._players:
            cls._players.append(player)
        else:
            raise ValueError(f'{player} already exists')

    @classmethod
    def players(cls):
        return cls._players
