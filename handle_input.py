def get_input(prompt: str, condition: callable):
    received_input = input(prompt).lower()
    if condition(received_input):
        return received_input
    else:
        raise ValueError


def check_name(user_input: str):
    conditions = (
        14 >= len(user_input) >= 2,
        all(ch.isalpha() or ch == ' ' for ch in user_input)
    )
    return all(conditions)


def check_kept_dice(user_input: str):
    valid_characters = '123456'
    or_conditions = (
        all(ch in valid_characters for ch in user_input),
        user_input == 'a',
        user_input == 'r'
    )
    conditions = (
        any(or_conditions),
        5 >= len(user_input) >= 1
    )
    return all(conditions)


def check_field(user_input: str):
    valid_fields = {
        'ones',
        'twos',
        'threes',
        'fours',
        'fives',
        'sixes',
        'three of a kind',
        'four of a kind',
        'full house',
        'small straight',
        'large straight',
        'yahtzee',
        'chance'
    }

    return user_input in valid_fields
