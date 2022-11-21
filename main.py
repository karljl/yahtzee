from engine import create_players, create_turn_keeper, game_loop


def main():
    create_players()
    turn_keeper = create_turn_keeper()
    game_loop(turn_keeper)


if __name__ == '__main__':
    main()
