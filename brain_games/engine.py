import prompt


def game_engine(RULE, game_logic):
    print('', 'Welcome to the Brain Games!', RULE, "", sep='\n')
    user_name = prompt.string('May I have your user_name? ')
    print(f'Hello, {user_name}!\n')
    for game_round in range(3):
        game_task, correct_answer = game_logic()
        user_answer = prompt.string(f'Question: {game_task}\nYour correct_answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong correct_answer ;(. '
                  f'Correct correct_answer was \'{correct_answer}\'.\n'
                  f'Let\'s try again, {user_name}!')
            break
    else:
        print(f'Congratulations, {user_name}!')
