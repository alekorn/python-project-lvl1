import prompt


def greet():
    print()
    print('Welcome to the Brain Games!')


def run():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    return name
