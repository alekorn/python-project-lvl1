import random


RULE = 'Answer "yes" if given number is prime. Otherwise correct_answer "no".'


def game_logic():
    game_task = random.randint(1, 99)
    prime_ints = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    )
    if game_task in prime_ints:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return game_task, correct_answer
