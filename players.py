from __future__ import annotations

from copy import deepcopy
from score import Scoreboard


class Player:

    def __init__(self, name: str):
        self.name = name
        self.scoreboard: Scoreboard = Scoreboard()

    def __eq__(self, other: Player):
        if isinstance(other, Player):
            return self.name == other.name
        raise TypeError(f'invalid comparison between {type(self)} and {type(other)}')

    def __repr__(self):
        return self.name


class PlayerDB:

    _players = []

    @classmethod
    def add(cls, player):
        cls._players.append(player)

    @classmethod
    def show(cls):
        return deepcopy(cls._players)
