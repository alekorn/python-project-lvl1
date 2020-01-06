import prompt


def greet():
    print('Welcome to the Brain Games!')


def run():
    print()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
