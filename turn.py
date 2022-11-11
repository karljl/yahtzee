from players import Player
from random import shuffle


class TurnKeeper:

    def __init__(self, players: list[Player]):
        self._players = players
        self._current_player_id: int = 0
        self._current_player: Player = self._get_current_player()

    def _get_current_player(self):
        return self._players[self._current_player_id]

    def _assign_current_player(self):
        self._current_player = self._get_current_player()

    def next_turn(self):
        if self._current_player_id != len(self._players) - 1:
            self._current_player_id += 1
        else:
            self._current_player_id = 0
        self._assign_current_player()

    @property
    def current_player(self):
        return self._current_player


def randomize_player_order(players: list[Player]):
    shuffle(players)
    return players
