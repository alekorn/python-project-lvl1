import prompt
import random
from brain_games.cli import run


def game_logic():
    print('Answer "yes" if number even otherwise answer "no".')
    print()
    name = run()
    for index in range(3):
        rand_int = random.randint(1, 99)
        answer = prompt.string(f'Question: {rand_int}\nYour answer: ')
        if rand_int % 2 == 0:
            correct_answer = 'no'
        elif rand_int % 2 != 0:
            correct_answer = 'yes'
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(.'
            'Correct answer was \'{correct_answer}\'./n'
            'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
