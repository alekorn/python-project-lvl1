import random

RULE = 'Answer "yes" if number even otherwise answer "no".'
START_RANGE = 1
END_RANGE = 99


def generate_round():
    game_task = random.randint(START_RANGE, END_RANGE)
    if game_task % 2 == 0:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return game_task, correct_answer
