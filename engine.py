from players import create_player, PlayerDB
from game_state import randomize_player_order, GameState
from dice import Dice, keep_dice, dice_roll_to_str, str_dice_roll_to_list_int
from score import CalculatePoints

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

randomized_order_players = randomize_player_order(PlayerDB.players())
game_state = GameState(randomized_order_players)
while True:

    all_kept_dice = ''
    roll_counter = 0
    current_player = game_state.current_player
    print(f"It 's {current_player}'s turn!")

    while True:
        roll = Dice().roll(5 - len(all_kept_dice))
        roll_counter += 1
        print(roll)
        if roll_counter != 3:
            kept_dice = keep_dice(roll)
            all_kept_dice += kept_dice
        else:
            all_kept_dice += dice_roll_to_str(roll)
        if len(all_kept_dice) == 5 or roll_counter == 3:
            break

    field_chosen = input('Please select the field you wish to add points to: ')  # TODO: implement getting input for choosing the field
    kept_dice_list = str_dice_roll_to_list_int(all_kept_dice)
    calculated_points = CalculatePoints(kept_dice_list, field_chosen).calculate_points()
    current_player.scoreboard.add_score(field_chosen, calculated_points)
    print(current_player.scoreboard.readable)
    game_state.next_turn()


# * Main game loop
#
#     ROLLING AND KEEPING (inner loop)
#         * The player rolls (5 - amount of previously kept dice) dice
#         * If the player has not yet rolled three times:
#                 The player chooses which dice to keep from rolled dice and all previously kept dice.
#           Else, all rolled dice are automatically kept.
#         * If len(kept dice) is 5 or number of rolls is 3:
#                 Break the inner loop.
#           Else, start the inner loop again.
#
#     CHOOSING THE FIELD TO ADD THE SCORE TO
#         * The player chooses to which field he wants to add the score to (f.e "Three of a kind").
#             - They can only choose the field if it is empty (except a special rule with the field "Yahtzee")
#         * The score is added to the player's scoreboard.
#         * If every player has rolled enough to assign points to every field in the scoreboard:
#                 Break the main game loop.
#            Else, it is next player's turn, go back to the beginning of the main game loop.
#
#     WHEN THE GAME IS DONE
#         * Calculate the total points of everybody
#         * Display the winner
#         * Ask if the user wants to play again

