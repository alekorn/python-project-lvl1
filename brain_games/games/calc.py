import random


def rule():
    return 'What is the result of the expression?'


def game_question():
    first_int = random.randint(1, 99)
    second_int = random.randint(1, 99)
    operator = random.randint(1, 3)
    if operator == 1:
        question = f'{first_int} + {second_int}'
        answer = str(first_int + second_int)
    elif operator == 2:
        question = f'{first_int} - {second_int}'
        answer = str(first_int - second_int)
    elif operator == 3:
        question = f'{first_int} * {second_int}'
        answer = str(first_int * second_int)
    return question, answer
