from random import randint


class Dice:
    """
    I modified the class, so it would always return list[int] even with one value. The question I asked in Slack
    about accepting multiple types as one parameter, can be avoided this way.
    """

    _sides: int = 6

    @classmethod
    def roll(cls, times: int):
        return [randint(1, cls._sides) for _ in range(times)]


def dice_roll_to_str(dice_roll: list[int]):
    """
    I created this function because the input from the user is always a string, so it's easier to compare against it if
    necessary, f.e when picking the dice to keep etc.

    I tried also the opposite way that the roll is always list[int] and I converted user input also to list[int],
    but I think this one makes more sense, and it is way easier to work with.

    Also, I use this function in score.py/CalculatePoints for calculating the points for small and large straights.
    """
    if isinstance(dice_roll, list) and all(isinstance(value, int) for value in dice_roll):
        return ''.join(map(str, dice_roll))
    else:
        raise ValueError('invalid values, expected list[int]')


def str_dice_roll_to_list_int(str_dice_roll: str):
    return [int(ch) for ch in str_dice_roll]


def keep_dice(rolled_dice: str):
    user_choice = input('Select the dice you want to keep: ')  # TODO: implement getting input for dice to keep
    # TODO: check if the dice that the user chose are valid
    return user_choice
