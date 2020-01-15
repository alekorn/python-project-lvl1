import random


RULE = 'What number is missing in the progression?'


def generate_round():
    progression_step = random.randint(1, 10)
    random_index = random.randint(1, 10)
    progression_index = random.randint(1, 10)
    game_task_list = []
    for index in range(10):
        if index == random_index:
            game_task_list.append('..')
            correct_answer = str(progression_index)
        else:
            game_task_list.append(progression_index)
        progression_index += progression_step
    game_task = ' '.join(list(map(str, game_task_list)))
    return game_task, correct_answer
