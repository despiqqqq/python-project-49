import random
import prompt
from brain_games.scripts.cli import welcome_user as welcome_user


def greet_user():
    name = welcome_user()
    return name


def ask_question():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    print(f'Question: {random_number1} {random_number2}')
    return random_number1, random_number2


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was"
              f" '{correct_answer}'.")
        return False


def main():
    name = greet_user()
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0

    while correct_answers < 3:
        number1, number2 = ask_question()
        correct_answer = get_gcd(number1, number2)
        user_answer = prompt.string('Your answer: ')
        if check_answer(int(user_answer), correct_answer):
            correct_answers += 1
        else:
            print(f"Let's try again, {name}!")
            break

    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
