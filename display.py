from score import Scoreboard


def display_readable_scoreboard(scoreboard: Scoreboard):
    player = f"{scoreboard.player}'s scoreboard".center(19)
    upper_section = '\n'.join(f'{key.title().ljust(18)}{val}' for key, val in scoreboard.upper_section.items())
    lower_section = '\n'.join(f'{key.title().ljust(18)}{val}' for key, val in scoreboard.lower_section.items())
    upper_section_bonus = 'Bonus' + 13 * ' ' + f'{scoreboard.upper_section_bonus()}'

    return f'{player}\n{upper_section}\n\n{upper_section_bonus}\n\n{lower_section}'


def display_dice(roll: str):
    return ' '.join(f'[{ch}]' for ch in roll)
