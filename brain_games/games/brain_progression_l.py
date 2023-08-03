from random import randint

game_q = 'What number is missing in the progression?'

min_count = 5
max_count = 10
min_r = 1
max_r = 100
min_s = 2
max_s = 17


def make_progression(first_element, elements_count, step):

    progression = [first_element]

    for i in range(elements_count):
        progression.append(progression[-1] + step)

    return progression


def make_game_data():

    elements_count = randint(min_count, max_count)
    first_element = randint(min_r, max_r)
    step = randint(min_s, max_s)

    progression = make_progression(first_element, elements_count, step)

    missing_element_index = randint(0, elements_count - 1)

    progression = list(map(str, progression))
    answer_game = progression[missing_element_index]
    progression[missing_element_index] = '..'
    progression = ' '.join(progression)

    question = f'{progression}'

    return answer_game, question