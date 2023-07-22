import random

from brain_games.scripts.cli import welcome_user as welcome_user


def generate_progression():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression


def hide_number(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_number = progression[hidden_index]
    progression[hidden_index] = '..'
    return hidden_number, progression


def main():
    name = welcome_user()
    print("What number is missing in the progression?")
    correct_answers = 0
    while correct_answers < 3:
        progression = generate_progression()
        hidden_number, progression_with_hidden = hide_number(progression)

        print("Question:", ' '.join(map(str, progression_with_hidden)))
        answer = input("Your answer: ")

        if answer == str(hidden_number):
            print("Correct!")
            correct_answers += 1
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer"
                                 " was '" + str(hidden_number) + "'.")
            print("Let's try again, " + name + "!")
            break

    print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
