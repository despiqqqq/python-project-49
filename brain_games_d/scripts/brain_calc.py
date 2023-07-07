import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    correct_answers = 0

    while correct_answers < 3:
        oper = random.randint(1, 3)  # определение случайной операции

        # Генерация первого случайного числа
        random_number1 = random.randint(1, 10)

        # Генерация второго случайного числа
        random_number2 = random.randint(1, 10)

        if oper == 1:
            print(f'Question: {random_number1} + {random_number2}')
            res = prompt.string('Your answer: ')
            if random_number1 + random_number2 == int(res):
                print('Correct!')
                correct_answers += 1
            else:
                print(f"'{res}' is wrong answer ;(. Correct answer was '{random_number1 + random_number2}'.")
                print(f"Let's try again, {name}!")
                return

        if oper == 2:
            print(f'Question: {random_number1} - {random_number2}')
            res = prompt.string('Your answer: ')
            if random_number1 - random_number2 == int(res):
                print('Correct!')
                correct_answers += 1
            else:
                print(f"'{res}' is wrong answer ;(. Correct answer was '{random_number1 - random_number2}'.")
                print(f"Let's try again, {name}!")
                return

        if oper == 3:
            print(f'Question: {random_number1} * {random_number2}')
            res = prompt.string('Your answer: ')
            if random_number1 * random_number2 == int(res):
                print('Correct!')
                correct_answers += 1
            else:
                print(f"'{res}' is wrong answer ;(. Correct answer was '{random_number1 * random_number2}'.")
                print(f"Let's try again, {name}!")
                return

    print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()