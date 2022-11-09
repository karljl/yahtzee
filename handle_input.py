def get_input(prompt: str, condition: callable, error_msg: str):
    received_input = input(prompt)
    if condition(received_input):
        return received_input
    else:
        raise ValueError(error_msg)


def check_name(user_input: str):
    conditions = (
        15 > len(user_input) > 1,
        all(ch.isalpha() or ch == ' ' for ch in user_input)
    )
    return all(conditions)
