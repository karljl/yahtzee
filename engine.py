from players import PlayerDB, create_player
from turn import TurnKeeper, randomize_player_order
from dice import Dice, DiceKeeper, dice_roll_to_str, keep_dice
from custom_exceptions import PlayerExistsError
from handle_input import get_input, check_kept_dice

MAX_PLAYERS: int = 2

for _ in range(MAX_PLAYERS):
    while True:
        try:
            new_player = create_player()
            PlayerDB.add(new_player)
        except PlayerExistsError:
            print('This name already exists. Please choose another name.')
        except ValueError:
            print('Invalid name.')
        else:
            print(f'Player {new_player} successfully created!')
            break

players_in_random_order = randomize_player_order(PlayerDB.players())
turn_keeper = TurnKeeper(players_in_random_order)

dice = Dice()

while True:

    dice_keeper = DiceKeeper()
    roll_counter = 0

    current_player = turn_keeper.current_player

    while True:

        times_to_roll: int = 5 - len(dice_keeper.kept_dice)

        if times_to_roll != 0:

            dice_roll = dice.roll(times_to_roll)
            dice_roll_str = dice_roll_to_str(dice_roll)

            print(f"It's {current_player}'s turn.")
            print(f'{current_player} rolled {dice_roll}.')

            if roll_counter != 2:

                while True:

                    try:
                        choose_dice_to_keep = get_input('Choose the dice you wish to keep: ', check_kept_dice)
                        user_choice = keep_dice(dice_roll_str, choose_dice_to_keep)
                    except ValueError:
                        print('Invalid values chosen!')
                    else:
                        break

            else:

                user_choice = keep_dice(dice_roll_str, dice_roll_str)
                print('Keeping dice automatically.')
                turn_keeper.next_turn()
                break

            dice_keeper.kept_dice = user_choice
            roll_counter += 1

        else:

            turn_keeper.next_turn()
            break
