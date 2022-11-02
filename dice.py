from random import randint


class Dice:

    _sides: int = 6

    @classmethod
    def roll(cls):
        return randint(1, cls._sides)

    @classmethod
    def roll_multiple(cls, times: int):
        return [cls.roll() for _ in range(times)]


def dice_roll_to_str(dice_roll: int | list[int]):
    if isinstance(dice_roll, int):
        return str(dice_roll)
    elif isinstance(dice_roll, list) and all(isinstance(value, int) for value in dice_roll):
        return ''.join(map(str, dice_roll))
    else:
        raise ValueError(f'invalid type: {type(dice_roll)}, expected int or list[int]')
