import random


def rule():
    return 'Answer "yes" if number even otherwise answer "no".'


def game_question():
    question = random.randint(1, 99)
    if question % 2 == 0:
        answer = 'no'
    elif question % 2 != 0:
        answer = 'yes'
    return question, answer
