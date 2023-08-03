import prompt


def ask_name_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    return name
