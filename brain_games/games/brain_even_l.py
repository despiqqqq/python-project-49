from random import randint

game_q = 'Answer "yes" if the number is even, otherwise answer "no".'

min0 = 0
max1 = 100


def is_even(num):
    return num % 2 == 0


def make_game_data():
    num_quest = randint(min0,max1)
    answer_game = 'yes' if is_even(num_quest) else 'no'

    question = f'{num_quest}'

    return answer_game, question
