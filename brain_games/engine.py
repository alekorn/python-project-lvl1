import prompt

GAME_ROUNDS = 3


def run(game):
    print()
    print('Welcome to the Brain Games!')
    print(game.RULE)
    print()
    user_name = prompt.string('May I have your user_name? ')
    print(f'Hello, {user_name}!\n')
    for game_round in range(GAME_ROUNDS):
        game_task, correct_answer = game.generate_round()
        user_answer = prompt.string(
            f'Question: {game_task}'
            f'\nYour answer: '
        )
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {user_name}!')
