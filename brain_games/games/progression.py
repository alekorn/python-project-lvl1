import random


def rule():
    return 'What number is missing in the progression?'


def game_question():
    progression_step = random.randint(1, 10)
    random_index = random.randint(1, 10)
    question_list = []
    index = 1
    for i in range(10):
        if i == random_index:
            question_list.append('..')
            answer  = str(index)
        else:
            question_list.append(index)
        index += progression_step
    question = ' '.join(list(map(str, question_list)))
    return question, answer
