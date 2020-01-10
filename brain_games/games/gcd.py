import random


def rule():
    return 'Find the greatest common divisor of given numbers.'


def game_question():
    first_int = random.randint(1, 99)
    second_int = random.randint(1, 99)
    question = f'{first_int} {second_int}'
    while first_int != 0 and second_int != 0:
        if first_int > second_int:
            first_int %= second_int
        else:
            second_int %= first_int
    answer = str(first_int + second_int)
    return question, answer
