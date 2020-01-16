import random

RULE = 'Answer "yes" if given number is prime. Otherwise correct_answer "no".'
START_RANGE = 1
END_RANGE = 99
PRIME_INTS = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    )


def generate_round():
    game_task = random.randint(START_RANGE, END_RANGE)
    if is_prime(game_task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return game_task, correct_answer


def is_prime(integer):
    return integer in PRIME_INTS
