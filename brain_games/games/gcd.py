import random

RULE = 'Find the greatest common divisor of given numbers.'
START_RANGE = 1
END_RANGE = 99


def generate_round():
    first_int = random.randint(START_RANGE, END_RANGE)
    second_int = random.randint(START_RANGE, END_RANGE)
    game_task = f'{first_int} {second_int}'
    correct_answer = str(gcd(first_int, second_int))
    return game_task, correct_answer


def gcd(first_int, second_int):
    while first_int != 0 and second_int != 0:
        if first_int > second_int:
            first_int %= second_int
        else:
            second_int %= first_int
    return first_int + second_int
