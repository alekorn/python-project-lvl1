import random
import operator


RULE = 'What is the result of the expression?'
START_RANGE = 1
END_RANGE = 99
OPERATORS = [
    ("*", operator.mul),
    ("+", operator.add),
    ("-", operator.sub),
]


def generate_round():
    random_int = random.randint(START_RANGE, END_RANGE)
    operator_str, operator_func = random.choice(OPERATORS)
    correct_answer = str(operator_func(first_int, second_int))
    game_task = f'{first_int} {operator_str} {second_int}'
    return game_task, correct_answer
