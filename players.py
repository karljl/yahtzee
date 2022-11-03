from __future__ import annotations

from score import Scoreboard
from copy import deepcopy
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Player:

    name: str = field(repr=True, compare=True)
    scoreboard: Scoreboard = Scoreboard()


class PlayerDB:

    _players = []

    @classmethod
    def add(cls, player):
        cls._players.append(player)

    @classmethod
    def get(cls):
        return deepcopy(cls._players)
