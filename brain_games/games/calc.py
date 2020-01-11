import random


RULE = 'What is the result of the expression?'


def game_logic():
    first_int = random.randint(1, 99)
    second_int = random.randint(1, 99)
    operator = random.randint(1, 3)
    if operator == 1:
        game_task = f'{first_int} + {second_int}'
        correct_answer = str(first_int + second_int)
    elif operator == 2:
        game_task = f'{first_int} - {second_int}'
        correct_answer = str(first_int - second_int)
    elif operator == 3:
        game_task = f'{first_int} * {second_int}'
        correct_answer = str(first_int * second_int)
    return game_task, correct_answer
