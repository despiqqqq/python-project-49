import operator
from random import randint, choice

GAME_RULES = 'What is the result of the expression?'

min0 = 0
max1 = 100
max2 = 100


def calculate_expression(num1, num2, operation):
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }

    return str(operations[operation](num1, num2))


def make_game_data():
    operations = ['+', '-', '*']

    num1 = randint(min0, max1)
    num2 = randint(min0, max2)
    operation = choice(operations)

    answer_game = calculate_expression(num1, num2, operation)

    question = f'{num1} {operation} {num2}'

    return answer_game, question
