import random


def rule():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_question():
    question = random.randint(1, 99)
    prime_ints = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    if question in prime_ints:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
