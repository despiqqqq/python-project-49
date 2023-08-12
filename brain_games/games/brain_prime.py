from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. ' \
    'Otherwise answer "no".'

min0 = 0
max1 = 1000


def is_prime(num):
    if num <= 1:
        return False
    denominator = 2
    while denominator <= num ** 0.5:
        if num % denominator == 0:
            return False

        denominator += 1
    else:
        return True


def make_game_data():

    quest_num = randint(min0, max1)

    answer_game = 'yes' if is_prime(quest_num) else 'no'

    question = f'{quest_num}'

    return answer_game, question
