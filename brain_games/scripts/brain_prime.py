import random

from brain_games import main as intro_main


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def greet_user():
    name = intro_main()
    return name


def ask_question():
    number = random.randint(1, 100)
    print("Question:", number)
    answer = input("Your answer: ")
    return (number, answer)


def check_answer(number, answer):
    if (answer == "yes" and is_prime(number)) or (answer == "no" and not is_prime(number)):
        print("Correct!")
        return True
    else:
        correct_answer = "yes" if is_prime(number) else "no"
        print("'" + answer + "' is wrong answer ;(. Correct answer was '" + correct_answer + "'.")
        return False


def main():
    name = greet_user()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    correct_answers = 0

    while correct_answers < 3:
        number, answer = ask_question()
        if check_answer(number, answer):
            correct_answers += 1
        else:
            print("Let's try again, " + name + "!")
            break

    print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
