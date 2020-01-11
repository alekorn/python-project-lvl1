import random


RULE = 'Answer "yes" if number even otherwise answer "no".'


def game_logic():
    game_task = random.randint(1, 99)
    if game_task % 2 == 0:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return game_task, correct_answer
