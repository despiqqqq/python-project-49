import prompt

c = 3


def play_game(module_game):
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    for i in range(c):
        answer_game, question = module_game.make_game_data()

        print(module_game.game_q)

        print(f'Question: {question}')
        answer_user = input('Your answer: ')

        if answer_user == answer_game:
            print('Correct!')
            continue
        else:
            print(f"'{answer_user}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer_game}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

    return None
