from random import randint


class Dice:

    _sides: int = 6

    @classmethod
    def roll(cls, times: int):
        return [randint(1, cls._sides) for _ in range(times)]


def dice_roll_to_str(dice_roll: list[int]):
    if isinstance(dice_roll, list) and all(isinstance(value, int) for value in dice_roll):
        return ''.join(map(str, dice_roll))
    else:
        raise ValueError('invalid values, expected list[int]')
