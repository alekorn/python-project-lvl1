import random


RULE = 'Find the greatest common divisor of given numbers.'


def generate_round():
    first_int = random.randint(1, 99)
    second_int = random.randint(1, 99)
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
