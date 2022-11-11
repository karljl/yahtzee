def get_input(prompt: str, condition: callable):
    received_input = input(prompt)
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
    conditions = (
        all(ch in valid_characters for ch in user_input),
        5 >= len(user_input) >= 1
    )
    return all(conditions)
