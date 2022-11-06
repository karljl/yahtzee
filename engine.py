from players import create_player, PlayerDB
from game_state import randomize_player_order

MAX_PLAYERS: int = 3

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


"""
* Main game loop

    ROLLING AND KEEPING (inner loop)
        * The player rolls (5 - amount of previously kept dice) dice
        * If the player has not yet rolled three times:
                The player chooses which dice to keep from rolled dice and all previously kept dice.
          Else, all rolled dice are automatically kept.
        * If len(kept dice) is 5 or number of rolls is 3:
                Break the inner loop.
          Else, start the inner loop again.

    CHOOSING THE FIELD TO ADD THE SCORE TO
        * The player chooses to which field he wants to add the score to (f.e "Three of a kind").
            - They can only choose the field if it is empty (except a special rule with the field "Yahtzee")
        * The score is added to the player's scoreboard.
        * If every player has rolled enough to assign points to every field in the scoreboard:
                Break the main game loop.
           Else, it is next player's turn, go back to the beginning of the main game loop.

    WHEN THE GAME IS DONE
        * Calculate the total points of everybody
        * Display the winner
        * Ask if the user wants to play again
"""