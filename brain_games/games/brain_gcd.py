from random import randint
from math import gcd


GAME_RULES = 'Find the greatest common divisor of given numbers.'

min0 = 1
max1 = 100
max2 = 100


def make_game_data():

    num1 = randint(min0, max1)
    num2 = randint(min0, max2)

    answer_game = str(gcd(num1, num2))

    question = f'{num1} {num2}'

    return answer_game, question
