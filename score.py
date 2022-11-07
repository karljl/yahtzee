from collections import Counter
from dice import dice_roll_to_str


class Scoreboard:

    def __init__(self):

        self._upper_section: dict = {
            'ones': 0,
            'twos': 0,
            'threes': 0,
            'fours': 0,
            'fives': 0,
            'sixes': 0,
        }

        self._lower_section: dict = {
            'three of a kind': 0,
            'four of a kind': 0,
            'full house': 0,
            'small straight': 0,
            'large straight': 0,
            'yahtzee': 0,
            'chance': 0,
        }

    @property
    def upper_section(self):
        return self._upper_section

    @property
    def lower_section(self):
        return self._lower_section

    def upper_section_bonus(self):
        return 35 if sum(self._upper_section.values()) >= 63 else 0

    def _upper_section_total(self):
        return sum(self._upper_section.values())

    def _lower_section_total(self):
        return sum(self._lower_section.values())

    @property
    def total_score(self):
        return sum(
            [
                self._upper_section_total(),
                self.upper_section_bonus(),
                self._lower_section_total()
            ]
        )

    def _add_points_to_upper_section(self, field: str, points: int):
        self._upper_section[field] += points

    def _add_points_to_lower_section(self, field: str, points: int):
        self._lower_section[field] += points

    def add_score(self, field: str, points: int):
        assign_section = {
            field in self._upper_section: self._add_points_to_upper_section,
            field in self._lower_section: self._add_points_to_lower_section,
        }

        try:
            assign_section[True](field, points)
        except KeyError:
            raise KeyError(f'invalid field: {field}')

    @property
    def readable(self):
        upper_section = '\n'.join(f'{key.title().ljust(18)}{val}' for key, val in self.upper_section.items())
        lower_section = '\n'.join(f'{key.title().ljust(18)}{val}' for key, val in self.lower_section.items())
        upper_section_bonus = 'Bonus' + 13 * ' ' + f'{self.upper_section_bonus()}'

        return f'{upper_section}\n\n{upper_section_bonus}\n\n{lower_section}'


class CalculatePoints:

    def __init__(self, roll: list[int], field: str):
        self._roll = roll
        self._field = field

    @property
    def _counter_values(self):
        return Counter(self._roll).values()

    def calculate_points(self):
        calculate_field = {
            'ones': self._for_ones,
            'twos': self._for_twos,
            'threes': self._for_threes,
            'fours': self._for_fours,
            'fives': self._for_fives,
            'sixes': self._for_sixes,
            'three of a kind': self._for_three_of_a_kind,
            'four of a kind': self._for_four_of_a_kind,
            'full house': self._for_full_house,
            'small straight': self._for_small_straight,
            'large straight': self._for_large_straight,
            'yahtzee': self._for_yahtzee,
            'chance': self._for_chance,
        }
        try:
            return calculate_field[self._field]()
        except KeyError:
            raise KeyError(f'invalid field {self._field}')

    def _for_ones(self):
        return self._roll.count(1)

    def _for_twos(self):
        return 2 * self._roll.count(2)

    def _for_threes(self):
        return 3 * self._roll.count(3)

    def _for_fours(self):
        return 4 * self._roll.count(4)

    def _for_fives(self):
        return 5 * self._roll.count(5)

    def _for_sixes(self):
        return 6 * self._roll.count(6)

    def _for_three_of_a_kind(self):
        return sum(self._roll) if 3 in self._counter_values else 0

    def _for_four_of_a_kind(self):
        return sum(self._roll) if 4 in self._counter_values else 0

    def _for_full_house(self):
        return 25 if 3 in self._counter_values and 2 in self._counter_values else 0

    # Since there are so few combos of straights, it is way easier to hardcode them than to come up with some
    # algorithm.

    def _for_small_straight(self):
        possible_straights = {'1234', '2345', '3456'}
        modified_result = ''.join(sorted(set(dice_roll_to_str(self._roll))))
        return 30 if any(combo in modified_result for combo in possible_straights) else 0

    def _for_large_straight(self):
        possible_straights = {'12345', '23456'}
        modified_result = ''.join(sorted(set(dice_roll_to_str(self._roll))))
        return 40 if any(combo in modified_result for combo in possible_straights) else 0

    def _for_yahtzee(self):
        return 50 if len(set(self._roll)) == 1 else 0

    def _for_chance(self):
        return sum(self._roll)



