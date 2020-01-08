import prompt
import brain_games.games


def game_engine(rule, game_question):
    print('', 'Welcome to the Brain Games!', rule(), "", sep='\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    for game_round in range(3):
        question, answer = game_question()
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
