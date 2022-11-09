from players import create_player, PlayerDB
from turnkeeper import randomize_player_order, TurnKeeper

MAX_PLAYERS: int = 2

for _ in range(MAX_PLAYERS):
    while True:
        new_player = create_player()
        try:
            PlayerDB.add(new_player)
        except ValueError:
            print(f'{new_player} already exists. Please choose another name.')
        else:
            break

players_in_random_order = randomize_player_order(PlayerDB.players())
turn_keeper = TurnKeeper(players_in_random_order)
