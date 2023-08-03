from random import randint

GAME_CONDITION = 'What number is missing in the progression?'

MIN_COUNT = 5
MAX_COUNT = 10
MIN_RANGE = 1
MAX_RANGE = 100
MIN_STEP = 2
MAX_STEP = 17


def make_progression(first_element, elements_count, step):

    progression = [first_element]

    for i in range(elements_count):
        progression.append(progression[-1] + step)

    return progression


def make_game_data():

    elements_count = randint(MIN_COUNT, MAX_COUNT)
    first_element = randint(MIN_RANGE, MAX_RANGE)
    step = randint(MIN_STEP, MAX_STEP)

    progression = make_progression(first_element, elements_count, step)

    missing_element_index = randint(0, elements_count - 1)

    progression = list(map(str, progression))
    answer_game = progression[missing_element_index]
    progression[missing_element_index] = '..'
    progression = ' '.join(progression)

    question = f'{progression}'

    return answer_game, question