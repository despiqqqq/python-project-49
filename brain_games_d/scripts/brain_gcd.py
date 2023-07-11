import prompt
import random
from brain_games import main as intro_main


def main():
    name = intro_main()
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0
    while correct_answers < 3:
        random_number1 = random.randint(1, 100)
        random_number2 = random.randint(1, 100)
        print(f'Question: {random_number1}  {random_number2}')
        while random_number2 != 0:
            random_number1, random_number2 = random_number2, random_number1 % random_number2
        res = prompt.string('Your answer: ')
        if int(res) == random_number1:
            correct_answers += 1
            print('Correct!')
        else:
            print(f"'{res}' is wrong answer ;(. Correct answer was '{random_number1}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
