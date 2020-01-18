import random

RULE = 'Answer "yes" if given number is prime. Otherwise correct_answer "no".'
START_RANGE = 1
END_RANGE = 99


def generate_round():
    game_task = random.randint(START_RANGE, END_RANGE)
    if is_prime(game_task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return game_task, correct_answer


def is_prime(integer):
    if (integer == 1):
        return False
    elif (integer == 2):
        return True
    else:
        for i in range(2, integer):
            if(integer % i == 0):
                return False
        return True
