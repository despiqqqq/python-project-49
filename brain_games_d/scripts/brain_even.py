import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    answer = True
    c = 0  # счетчик правильных ответов

    while answer is True:
        random_number = random.randint(1, 1000)
        print(f'Question: {random_number}')
        res = prompt.string('Your answer: ')

        if (random_number % 2 == 0 and res == 'yes') or (random_number % 2 == 1 and res == 'no'):
            print('Correct!')
            c += 1
            if c == 3:
                print(f"Congratulations, {name}!")
                break
            continue
        else:
            print(f"Let's try again, {name}!")
            break


if __name__ == '__main__':
    main()
