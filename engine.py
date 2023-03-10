from players import PlayerDB, create_player
from turn import TurnKeeper, randomize_player_order
from dice import dice, DiceKeeper, dice_roll_to_str, keep_dice
from custom_exceptions import PlayerExistsError, FieldAlreadyUsedError
from handle_input import get_input, check_kept_dice, check_field
from score import PointsCalculator
from display import display_readable_scoreboard, display_dice
from constants import MAX_PLAYERS


def create_players():
    for _ in range(MAX_PLAYERS):
        while True:
            try:
                new_player = create_player()
                PlayerDB.add(new_player)
            except PlayerExistsError:
                print('This name already exists. Please choose another name.')
                print()
            except ValueError:
                print('Invalid name.')
                print()
            else:
                print(f'Player {new_player} successfully created!')
                print()
                break


def create_turn_keeper():
    players_in_random_order = randomize_player_order(PlayerDB.players())
    turn_keeper = TurnKeeper(players_in_random_order)
    return turn_keeper


def game_loop(turn_keeper: TurnKeeper):
    while True:
        dice_keeper = DiceKeeper()
        roll_counter = 0

        current_player = turn_keeper.current_player

        while True:
            times_to_roll: int = 5 - len(dice_keeper.kept_dice)

            if times_to_roll != 0:
                dice_roll = dice.roll(times_to_roll)
                dice_keeper.rolled_dice = dice_roll_to_str(dice_roll)
                print(f"It's {current_player}'s turn.")
                print(f'{current_player} rolled: {display_dice(dice_keeper.rolled_dice)}.')

                if dice_keeper.is_kept_dice:
                    print(f'Previously kept dice: {display_dice(dice_keeper.kept_dice)}')

                if roll_counter != 2:
                    while True:
                        try:
                            choose_dice_to_keep = get_input('Choose the dice you wish to keep: ', check_kept_dice)
                            user_choice_kept_dice = keep_dice(dice_keeper.rolled_dice, choose_dice_to_keep)
                        except ValueError:
                            print('Invalid values chosen.')
                        else:
                            if user_choice_kept_dice == 'r':
                                if dice_keeper.is_kept_dice:
                                    dice_keeper.release_kept_dice()
                                    print(f'All available dice: {display_dice(dice_keeper.rolled_dice)}')
                                else:
                                    print('There are no previously rolled dice to release.')
                            else:
                                break

                else:
                    user_choice_kept_dice = keep_dice(dice_keeper.rolled_dice, dice_keeper.rolled_dice)
                    dice_keeper.kept_dice = user_choice_kept_dice
                    print('Keeping the remaining dice automatically.')
                    print(display_dice(dice_keeper.kept_dice))
                    break

                if user_choice_kept_dice != 'n':
                    dice_keeper.kept_dice = user_choice_kept_dice
                    print(f'{current_player} kept: {display_dice(dice_keeper.kept_dice)}')
                else:
                    print(f'{current_player} did not keep any dice.')
                roll_counter += 1

            else:
                break

        while True:
            try:
                user_choice_field = get_input('Please choose the field you wish to add the points to: ', check_field)
            except ValueError:
                print('Invalid field.')
            else:
                points_calculator = PointsCalculator(dice_keeper.kept_dice, user_choice_field)
                points = points_calculator.calculate_points()
                try:
                    current_player.scoreboard.add_score(user_choice_field, points)
                except FieldAlreadyUsedError:
                    print('This field is already used.')
                else:
                    print(display_readable_scoreboard(current_player.scoreboard))
                    turn_keeper.next_turn()
                    break
