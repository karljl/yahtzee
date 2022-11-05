from __future__ import annotations

from score import Scoreboard
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Player:
    """
    I just learned a bit about dataclasses and since at least at the moment there is no functionality in the class, I
    figured it would be a good place to try it.
    """

    name: str = field(compare=True)
    scoreboard: Scoreboard = Scoreboard()

    def __repr__(self):
        return self.name


def create_player(player_name: str):  # TODO: implement getting input for player name
    new_player = Player(player_name)
    PlayerDB.add(new_player)


class PlayerDB:

    _players = []

    @classmethod
    def add(cls, player):
        cls._players.append(player)

    @classmethod
    def players(cls):
        return cls._players
