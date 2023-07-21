import prompt
import random
from brain_games.scripts.cli import welcome_user as welcome_user


def generate_question():
    oper = random.randint(1, 3)  # определение случайной операции

    # Генерация первого случайного числа
    random_number1 = random.randint(1, 10)

    # Генерация второго случайного числа
    random_number2 = random.randint(1, 10)

    if oper == 1:
        question = f'Question: {random_number1} + {random_number2}'
        correct_answer = str(random_number1 + random_number2)
    elif oper == 2:
        question = f'Question: {random_number1} - {random_number2}'
        correct_answer = str(random_number1 - random_number2)
    else:
        question = f'Question: {random_number1} * {random_number2}'
        correct_answer = str(random_number1 * random_number2)

    return question, correct_answer


def main():
    name = intro_main()
    print('What is the result of the expression?')
    correct_answers = 0

    while correct_answers < 3:
        question, correct_answer = generate_question()
        print(question)
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was"
                  f" '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
