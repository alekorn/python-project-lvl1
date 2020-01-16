import random

RULE = 'What number is missing in the progression?'
START_RANGE = 1
END_RANGE = 10


def generate_round():
    progression_step = random.randint(START_RANGE, END_RANGE)
    random_index = random.randint(START_RANGE, END_RANGE)
    progression_index = random.randint(START_RANGE, END_RANGE)
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
