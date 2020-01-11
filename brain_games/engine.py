import prompt


def game_engine(RULE, game_logic):
    print('', 'Welcome to the Brain Games!', RULE, "", sep='\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    for game_round in range(3):
        question, answer = game_logic()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if answer == user_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{answer}\'.\n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
