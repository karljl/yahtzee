from random import randint


class Dice:

    def __init__(self, sides: int):
        self._sides = sides

    def roll(self, times: int):
        return [randint(1, self._sides) for _ in range(times)]


dice = Dice(6)


class DiceKeeper:

    def __init__(self):
        self._kept_dice: str = ''
        self._rolled_dice: str = ''

    @property
    def rolled_dice(self):
        return self._rolled_dice

    @rolled_dice.setter
    def rolled_dice(self, value):
        self._rolled_dice = value

    @property
    def kept_dice(self):
        return self._kept_dice

    @kept_dice.setter
    def kept_dice(self, value):
        self._kept_dice += value

    def release_kept_dice(self):
        self._rolled_dice += self._kept_dice
        self._kept_dice = ''

    @property
    def is_kept_dice(self):
        return len(self._kept_dice) != 0


def dice_roll_to_str(dice_roll: list[int]):
    if isinstance(dice_roll, list) and all(isinstance(value, int) for value in dice_roll):
        return ''.join(map(str, dice_roll))
    else:
        raise ValueError('invalid value, expected list[int]')


def keep_dice(rolled_dice: str, user_choice: str):
    if user_choice == 'a':
        return rolled_dice

    if user_choice not in {'r', 'n'}:
        for value in user_choice:
            if user_choice.count(value) > rolled_dice.count(value):
                raise ValueError

    return user_choice
