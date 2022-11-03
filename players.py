from __future__ import annotations

from score import Scoreboard
from copy import deepcopy
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Player:
    """
    I just learned a bit about dataclasses and since at least at the moment there is no functionality in the class, I
    figured it would be a good place to try it.
    """

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
